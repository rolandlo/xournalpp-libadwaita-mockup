import Gtk from "gi://Gtk";
import Adw from "gi://Adw";
import Gio from "gi://Gio";

const button = workbench.builder.get_object("button");
const marker = workbench.builder.get_object("marker");
const popover = workbench.builder.get_object("button");
const button_yellow = workbench.builder.get_object("button_yellow");
const button_green = workbench.builder.get_object("button_green");
const button_red = workbench.builder.get_object("button_red");
const scale_thickness = workbench.builder.get_object("scale_thickness");
const scale_opacity = workbench.builder.get_object("scale_opacity");

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

for (const [value, label] of Object.entries(marks_thickness)) {
  scale_thickness.add_mark(value, Gtk.PositionType.ABOVE, "");
}

for (const [value, label] of Object.entries(marks_opacity)) {
  scale_opacity.add_mark(value, Gtk.PositionType.ABOVE, label);
}

button.connect("clicked", () => {
  console.log("Button selected");
});

button_yellow.connect("clicked", (_self) => {
  change(_self, "@yellow_5").catch(console.error);
});

button_green.connect("clicked", (_self) => {
  change(_self, "@green_1").catch(console.error);
});

button_red.connect("clicked", (_self) => {
  change(_self, "@red_1").catch(console.error);
});

async function change(_self, color) {
  console.log(`Color ${color} chosen`);

  const cssString = `#marker { color: ${color}; } `;
  const provider = new Gtk.CssProvider();
  provider.load_from_string(cssString);

  const context = marker.get_style_context();
  context.add_provider(provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION);
}

