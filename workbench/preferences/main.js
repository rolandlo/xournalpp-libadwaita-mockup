import Gtk from "gi://Gtk";
import Gio from "gi://Gio";
import Adw from "gi://Adw";

Gio._promisify(Gtk.FileDialog.prototype, "open", "open_finish");
Gio._promisify(
  Gtk.FileDialog.prototype,
  "select_folder",
  "select_folder_finish",
);

const style_manager = Adw.StyleManager.get_default();

const { win_prefs, sw_dark_theme, placeholders } = workbench.build({
  // signal handlers
  checkTex(_self) {
    const toast = new Adw.Toast({
      title: "Sample LaTeX file generated successfully",
    });

    win_prefs.add_toast(toast);
  },
  toggleDark(_self) {
    console.log("Toggle Dark");
    if (_self.active) {
      style_manager.color_scheme = Adw.ColorScheme.FORCE_DARK;
    } else {
      style_manager.color_scheme = Adw.ColorScheme.FORCE_LIGHT;
    }
  },
  selectAudioFolder(_self) {
    selectFolder(_self).catch(console.error);
  },
  selectTemplate(_self) {
    openFile(_self).catch(console.error);
  },

  // bindings
  showCustom(_self, enable, method) {
    return method.string === "Custom";
  },
  showMean(_self, method) {
    return method.string === "Arithmetic Mean";
  },
  showGauss(_self, method) {
    return method.string === "Gaussian weights";
  },
  showDeadZone(_self, method) {
    return method.string === "Dead Zone";
  },
  showInertia(_self, method) {
    return method.string === "Inertia";
  },
});

sw_dark_theme.active = style_manager.dark;

placeholders.set_label(
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

async function openFile(_self) {
  const dialog_for_file = new Gtk.FileDialog();
  const file = await dialog_for_file.open(workbench.window, null);
  const info = file.query_info(
    "standard::name",
    Gio.FileQueryInfoFlags.NONE,
    null,
  );
  _self.get_child().set_label(info.get_name());
}

async function selectFolder(_self) {
  const dialog_for_folder = new Gtk.FileDialog();
  const folder = await dialog_for_folder.select_folder(workbench.window, null);
  const info = folder.query_info(
    "standard::name",
    Gio.FileQueryInfoFlags.NONE,
    null,
  );
  _self.get_child().set_label(info.get_name());
}

win_prefs.present();

