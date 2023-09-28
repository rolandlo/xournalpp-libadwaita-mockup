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
      "scale_opacity",
      "im_linestyle",
      "im_drawingtype",
    ],
  },
  class Marker extends Gtk.Grid {
    // register signal handlers and other symbols
    constructor(color, linestyle, drawingtype) {
      super();
      this.color = color;
      this.linestyle = linestyle;
      set_css_property(this._marker, "color", color);
      this._im_linestyle.set_from_icon_name(`line-style-${linestyle}-symbolic`);
      this._im_drawingtype.set_from_icon_name(`${drawingtype}-symbolic`);
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
      console.log(_self.name);
      let color = "";

      switch (_self.name) {
        case "button_green":
          color = "#8ff0a4";
          break;
        case "button_yellow":
          color = "#e5a50a";
          break;
        case "button_red":
          color = "#f66151";
          break;
      }
      set_css_property(this._marker, "color", color).catch(console.error);
    }

    on_linestyle_button_clicked(_self) {
      console.log(_self.name);

      switch (_self.name) {
        case "linestyle_plain":
          this._im_linestyle.set_from_icon_name("line-style-plain-symbolic");
          break;
        case "linestyle_dash":
          this._im_linestyle.set_from_icon_name("line-style-dash-symbolic");
          break;
        case "linestyle_dash_dot":
          this._im_linestyle.set_from_icon_name("line-style-dash-dot-symbolic");
          break;
        case "linestyle_dot":
          this._im_linestyle.set_from_icon_name("line-style-dot-symbolic");
          break;
      }
    }

    on_drawingtype_button_clicked(_self) {
      console.log(_self.name);

      switch (_self.name) {
        case "drawingtype_rect":
          this._im_drawingtype.set_from_icon_name("rect-symbolic");
          break;
        case "drawingtype_ellipse":
          this._im_drawingtype.set_from_icon_name("ellipse-symbolic");
          break;
        case "drawingtype_arrow":
          this._im_drawingtype.set_from_icon_name("arrow-symbolic");
          break;
        case "drawingtype_doublearrow":
          this._im_drawingtype.set_from_icon_name("double-arrow-symbolic");
          break;
        case "drawingtype_line":
          this._im_drawingtype.set_from_icon_name("line-symbolic");
          break;
        case "drawingtype_coordinatesystem":
          this._im_drawingtype.set_from_icon_name("coordinate-system-symbolic");
          break;
        case "drawingtype_spline":
          this._im_drawingtype.set_from_icon_name("spline-symbolic");
          break;
        case "drawingtype_shaperecognizer":
          this._im_drawingtype.set_from_icon_name("shape-recognizer-symbolic");
          break;
      }
    }
  },
);

const box = new Gtk.Box({ spacing: 24 });
const marker1 = new Marker("#8ff0a4", "dash-dot", "arrow");
const marker2 = new Marker("#f66151", "plain", "ellipse");
marker1._scale_opacity.set_value(10);
box.append(marker1);
box.append(marker2);

workbench.preview(box);

