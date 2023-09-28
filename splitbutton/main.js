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

const palette_names = [
  "yellow3",
  "orange3",
  "purple2",
  "green2",
  "blue2",
  "dark2",
  "green5",
  "red3",
  "blue4",
];
const palette_colors = [
  "#f6d32d",
  "#ff7800",
  "#c061cb",
  "#57e389",
  "#62a0ea",
  "#5e5c64",
  "#26a269",
  "#e01b24",
  "#1c71d8",
];

async function set_css_property(widget, property, value) {
  const cssString = `#${widget.name} { ${property}: ${value}; } `;
  const provider = new Gtk.CssProvider();
  provider.load_from_string(cssString);

  const context = widget.get_style_context();
  context.add_provider(provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION);
}

function hex_from_color_and_opacity(color, opacity) {
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
      "button_green",
      "button_red",
      "button_color_chooser",
      "scale_thickness",
      "ad_thickness",
      "scale_opacity",
      "ad_opacity",
      "im_linestyle",
      "im_drawingtype",
      "sw_filled",
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
      set_css_property(
        this._marker,
        "color",
        hex_from_color_and_opacity(color, marker_opacity),
      );
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
    }

    on_button_clicked() {
      console.log("Split button child clicked");
    }

    on_color_button_clicked(_self) {
      switch (_self.name) {
        case "button_green":
          this.color = "#8ff0a4";
          break;
        case "button_yellow":
          this.color = "#e5a50a";
          break;
        case "button_red":
          this.color = "#f66151";
          break;
        case "color-chooser": {
          const rgba = _self.get_rgba();
          const r = Math.floor(rgba.red * 255);
          const g = Math.floor(rgba.green * 255);
          const b = Math.floor(rgba.blue * 255);
          this.color = `#${r.toString(16)}${g.toString(16)}${b.toString(16)}`;
          break;
        }
      }
      set_css_property(
        this._marker,
        "color",
        hex_from_color_and_opacity(this.color, this.marker_opacity),
      ).catch(console.error);
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
        hex_from_color_and_opacity(this.color, this.marker_opacity),
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

