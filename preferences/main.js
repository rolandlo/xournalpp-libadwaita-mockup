import Gtk from "gi://Gtk";
import Gio from "gi://Gio";
import Adw from "gi://Adw";

Gio._promisify(Gtk.FileDialog.prototype, "open", "open_finish");

const btn_check = workbench.builder.get_object("btn_check");
const style_manager = Adw.StyleManager.get_default();
const pref_window = workbench.builder.get_object("win_prefs");
const row_generation_info = workbench.builder.get_object("row_generation_info");
const info_latex_generation = workbench.builder.get_object(
  "info_latex_generation",
);
const info_latex_generation_back = workbench.builder.get_object(
  "info_latex_generation_back",
);
const button_template = workbench.builder.get_object("btn_template");
const sw_dark_theme = workbench.builder.get_object("sw_dark_theme");

sw_dark_theme.active = style_manager.dark;

sw_dark_theme.connect("notify::active", () => {
  console.log("Connected");
  // When the Switch is toggled, set the color scheme
  if (sw_dark_theme.active) {
    style_manager.color_scheme = Adw.ColorScheme.FORCE_DARK;
  } else {
    style_manager.color_scheme = Adw.ColorScheme.FORCE_LIGHT;
  }
});

row_generation_info.connect("activated", () => {
  pref_window.present_subpage(info_latex_generation);
});

info_latex_generation_back.connect("clicked", () => {
  pref_window.close_subpage();
});

async function openFile() {
  const dialog_for_file = new Gtk.FileDialog();
  const file = await dialog_for_file.open(workbench.window, null);
  const info = file.query_info(
    "standard::name",
    Gio.FileQueryInfoFlags.NONE,
    null,
  );
  const button_content = button_template.get_child();
  button_content.set_label(info.get_name());
}

button_template.connect("clicked", () => {
  openFile().catch(console.error);
});

btn_check.connect("clicked", () => {
  const toast = new Adw.Toast({
    title: "Sample LaTeX file generated successfully",
  });

  pref_window.add_toast(toast);
});
