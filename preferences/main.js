import Adw from "gi://Adw";

const style_manager = Adw.StyleManager.get_default();
const pref_window = workbench.builder.get_object("win_prefs");
const row_generation_info = workbench.builder.get_object("row_generation_info");
const info_latex_generation = workbench.builder.get_object(
  "info_latex_generation",
);
const info_latex_generation_back = workbench.builder.get_object(
  "info_latex_generation_back",
);

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

