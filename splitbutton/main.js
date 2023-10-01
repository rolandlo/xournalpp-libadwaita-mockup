import GObject from "gi://GObject";
import Gtk from "gi://Gtk";
import Adw from "gi://Adw";
import Gio from "gi://Gio";

const marks_thickness = {
  0.132: "finer", // ln(0.42) + 1
  0.837: "fine", // ln(0.85) + 1
  1.344: "medium", // ln(1.41) + 1
  1.815: "thick", // ln(2.26) + 1
  2.735: "thicker", // ln(5.67) + 1
};

const marks_opacity = {
  0: "0%",
  50: "50%",
  100: "100%",
};

const palette = [];
palette.push({ name: "yellow3", color: "#f6d32d" });
palette.push({ name: "orange3", color: "#ff7800" });
palette.push({ name: "purple2", color: "#c061cb" });
palette.push({ name: "green2", color: "#57e389" });
palette.push({ name: "blue2", color: "#62a0ea" });
palette.push({ name: "dark2", color: "#5e5c64" });
palette.push({ name: "green5", color: "#26a269" });
palette.push({ name: "red3", color: "#e01b24" });
palette.push({ name: "blue4", color: "#1c71d8" });

function set_css_property(widget, property, value) {
  const cssString = `#${widget.name} { ${property}: ${value}; } `;
  const provider = new Gtk.CssProvider();
  provider.load_from_string(cssString);

  const context = widget.get_style_context();
  context.add_provider(provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION);
}

function hex(color, opacity) {
  const alpha_decimal = Math.floor((opacity + 100) * 1.275);
  const alpha = alpha_decimal.toString(16);
  return `${color}${alpha}`;
}

const Marker = GObject.registerClass(
  {
    GTypeName: "Marker",
    Template: workbench.template,
    InternalChildren: [
      "button",
      "marker",
      "popover",
      "scale_thickness",
      "ad_thickness",
      "scale_opacity",
      "ad_opacity",
      "im_linestyle",
      "im_drawingtype",
      "sw_filled",
      "color_box",
    ],
  },
  class Marker extends Gtk.Grid {
    // register signal handlers and other symbols
    constructor(
      color,
      fill,
      marker_opacity,
      linestyle,
      thickness,
      drawingtype,
    ) {
      super();
      this.color = color;
      this.marker_opacity = marker_opacity;
      this._sw_filled.active = fill;
      set_css_property(this._marker, "color", hex(color, marker_opacity));
      this._im_linestyle.set_from_icon_name(`line-style-${linestyle}`);
      this._im_drawingtype.set_from_icon_name(`${drawingtype}`);
      this._ad_opacity.set_value(marker_opacity);
      this._ad_thickness.set_value(thickness);
      for (const [value, label] of Object.entries(marks_thickness)) {
        this._scale_thickness.add_mark(value, Gtk.PositionType.ABOVE, "");
      }

      for (const [value, label] of Object.entries(marks_opacity)) {
        this._scale_opacity.add_mark(value, Gtk.PositionType.ABOVE, label);
      }

      for (let i = 0; i < palette.length; i++) {
        const button = new Gtk.Button();
        button.set_name(palette[i].name);
        button.add_css_class("circular");
        set_css_property(button, "background-color", palette[i].color);
        button.connect("clicked", (_self) => {
          const entry = palette.find((element) => element.name === _self.name);
          set_css_property(this._marker, "color", entry.color);
        });
        this._color_box.append(button);
      }

      const color_dialog = new Gtk.ColorDialog();
      color_dialog.set_with_alpha(false);
      const color_button = new Gtk.ColorDialogButton();
      color_button.set_dialog(color_dialog);
      color_button.set_name("color-chooser");
      color_button.connect("notify::rgba", (_self) => {
        const rgba = _self.get_rgba();
        const r = Math.floor(rgba.red * 255);
        const g = Math.floor(rgba.green * 255);
        const b = Math.floor(rgba.blue * 255);
        this.color = `#${r.toString(16)}${g.toString(16)}${b.toString(16)}`;
        set_css_property(
          this._marker,
          "color",
          hex(this.color, this.marker_opacity),
        );
      });
      this._color_box.append(color_button);
    }

    on_button_clicked() {
      console.log("Split button child clicked");
    }

    on_linestyle_button_clicked(_self) {
      switch (_self.name) {
        case "linestyle_plain":
          this._im_linestyle.set_from_icon_name("line-style-plain");
          break;
        case "linestyle_dash":
          this._im_linestyle.set_from_icon_name("line-style-dash");
          break;
        case "linestyle_dash_dot":
          this._im_linestyle.set_from_icon_name("line-style-dash-dot");
          break;
        case "linestyle_dot":
          this._im_linestyle.set_from_icon_name("line-style-dot");
          break;
      }
    }

    on_drawingtype_button_clicked(_self) {
      switch (_self.name) {
        case "drawingtype_rect":
          this._im_drawingtype.set_from_icon_name("rect");
          break;
        case "drawingtype_ellipse":
          this._im_drawingtype.set_from_icon_name("ellipse");
          break;
        case "drawingtype_arrow":
          this._im_drawingtype.set_from_icon_name("arrow");
          break;
        case "drawingtype_doublearrow":
          this._im_drawingtype.set_from_icon_name("double-arrow");
          break;
        case "drawingtype_line":
          this._im_drawingtype.set_from_icon_name("line");
          break;
        case "drawingtype_coordinatesystem":
          this._im_drawingtype.set_from_icon_name("coordinate-system");
          break;
        case "drawingtype_spline":
          this._im_drawingtype.set_from_icon_name("spline");
          break;
        case "drawingtype_shaperecognizer":
          this._im_drawingtype.set_from_icon_name("shape-recognizer");
          break;
      }
    }

    on_filled_set(_self, state) {
      if (state) {
        this._marker.set_from_icon_name("marker-filled-symbolic");
      } else {
        this._marker.set_from_icon_name("marker-not-filled-symbolic");
      }
    }

    on_thickness_changed(_self) {
      this.thickness = _self.value;
      set_css_property(
        this._im_linestyle,
        "-gtk-icon-transform",
        `scale(${(this.thickness + 2.0) / 3.0})`,
      );
    }

    on_opacity_changed(_self) {
      this.marker_opacity = _self.value;
      set_css_property(
        this._marker,
        "color",
        hex(this.color, this.marker_opacity),
      );
    }
  },
);

const box = new Gtk.Box({ spacing: 24 });
const marker1 = new Marker(
  "#8ff0a4", // color
  true, // filled
  50.0, // opacity
  "dash-dot", // line style
  Object.keys(marks_thickness)[1], // thickness
  "arrow", // drawing type
);
const marker2 = new Marker(
  "#f66151",
  false,
  80.0,
  "plain",
  Object.keys(marks_thickness)[3],
  "ellipse",
);
marker1._ad_opacity.set_value(50.0);
box.append(marker1);
box.append(marker2);

workbench.preview(box);

