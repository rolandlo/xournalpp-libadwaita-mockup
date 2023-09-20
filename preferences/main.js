const pref_window = workbench.builder.get_object("win_prefs");
const row_generation_info = workbench.builder.get_object("row_generation_info");
const info_latex_generation = workbench.builder.get_object(
  "info_latex_generation",
);
const info_latex_generation_back = workbench.builder.get_object(
  "info_latex_generation_back",
);

row_generation_info.connect("activated", () => {
  pref_window.present_subpage(info_latex_generation);
});

info_latex_generation_back.connect("clicked", () => {
  pref_window.close_subpage();
});

