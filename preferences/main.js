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
const lbl_placeholders = workbench.builder.get_object("placeholders");

lbl_placeholders.set_label(
  `
%a    Abbreviated weekday name (e.g. Thu)
%A    Full weekday name (e.g. Thursday)
%b    Abbreviated month name (e.g. Aug)
%B    Full month name (e.g. August)
%c    Date and time representation (e.g. Thu Aug 23 14:55:02 2001)
%d    Day of the month (01-31)
%F    Date representation (e.g. 2001-08-23)
%H    Hour in 24h format (00-23)
%I    Hour in 12h format (01-12)
%j    Day of the year (001-366)
%m    Month as a decimal number (01-12)
%M    Minute (00-59)
%p    AM or PM designation (e.g. PM)
%S    Second (00-61)
%U    Week number with the first Sunday as the first day of week one (00-53)
%w    Weekday as a decimal number with Sunday as 0 (0-6)
%W    Week number with the first Monday as the first day of week one (00-53)
%x    Date representation (e.g. 08/23/01)
%X    Time representation (e.g. 14:55:02)
%y    Year, last two digits (00-99)
%Y    Year (e.g. 2001)
%Z    Timezone name or abbreviation (e.g. CDT)
%%    A % sign
`,
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

