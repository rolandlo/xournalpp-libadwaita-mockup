import gi
from .util import get_resource_path

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw


@Gtk.Template(resource_path=get_resource_path("ui/preferences.ui"))
class Preferences(Adw.PreferencesWindow):
    __gtype_name__ = "Preferences"


@Gtk.Template(resource_path=get_resource_path("ui/preferences_audio.ui"))
class AudioPage(Adw.PreferencesPage):
    __gtype_name__ = "AudioPage"

    audio_folder_button_content = Gtk.Template.Child()

    @Gtk.Template.Callback()
    def selectAudioFolder(self, button):
        dialog = Gtk.FileDialog()
        folder = dialog.select_folder(None, None, self.on_folder_selected)

    def on_folder_selected(self, dialog, result):
        folder = dialog.select_folder_finish(result)
        self.audio_folder_button_content.set_label(folder.get_basename())


@Gtk.Template(resource_path=get_resource_path("ui/preferences_defaults.ui"))
class DefaultsPage(Adw.PreferencesPage):
    __gtype_name__ = "DefaultsPage"


@Gtk.Template(resource_path=get_resource_path("ui/preferences_drawing.ui"))
class DrawingPage(Adw.PreferencesPage):
    __gtype_name__ = "DrawingPage"


@Gtk.Template(resource_path=get_resource_path("ui/preferences_input.ui"))
class InputPage(Adw.PreferencesPage):
    __gtype_name__ = "InputPage"

    @Gtk.Template.Callback()
    def showMean(self, dialog, method):
        return method.get_string() == "Arithmetic Mean"

    @Gtk.Template.Callback()
    def showGauss(self, dialog, method):
        return method.get_string() == "Gaussian weights"

    @Gtk.Template.Callback()
    def showDeadZone(self, dialog, method):
        return method.get_string() == "Dead Zone"

    @Gtk.Template.Callback()
    def showInertia(self, dialog, method):
        return method.get_string() == "Inertia"


@Gtk.Template(resource_path=get_resource_path("ui/preferences_language.ui"))
class LanguagePage(Adw.PreferencesPage):
    __gtype_name__ = "LanguagePage"


@Gtk.Template(resource_path=get_resource_path("ui/preferences_latex.ui"))
class LaTexPage(Adw.PreferencesPage):
    __gtype_name__ = "LaTeXPage"

    template_button_content = Gtk.Template.Child()

    @Gtk.Template.Callback()
    def checkTex(self, button):
        toast = Adw.Toast(title="Sample LaTeX file generated successfully")
        button.get_root().add_toast(toast)

    @Gtk.Template.Callback()
    def selectTemplate(self, button):
        dialog = Gtk.FileDialog()
        filter = Gtk.FileFilter()
        filter.set_name(".tex file")
        filter.add_pattern("*.tex")
        dialog.set_default_filter(filter)
        dialog.open(None, None, self.on_file_selected)

    def on_file_selected(self, dialog, result):
        file = dialog.open_finish(result)
        self.template_button_content.set_label(file.get_basename())


@Gtk.Template(resource_path=get_resource_path("ui/preferences_load_save.ui"))
class LoadSavePage(Adw.PreferencesPage):
    __gtype_name__ = "LoadSavePage"

    placeholders = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.placeholders.set_label(
            """
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
"""
        )


@Gtk.Template(resource_path=get_resource_path("ui/preferences_mouse.ui"))
class MousePage(Adw.PreferencesPage):
    __gtype_name__ = "MousePage"


@Gtk.Template(resource_path=get_resource_path("ui/preferences_stylus.ui"))
class StylusPage(Adw.PreferencesPage):
    __gtype_name__ = "StylusPage"


@Gtk.Template(resource_path=get_resource_path("ui/preferences_touchscreen.ui"))
class TouchscreenPage(Adw.PreferencesPage):
    __gtype_name__ = "TouchscreenPage"

    @Gtk.Template.Callback()
    def showCustom(self, entryrow, method):
        return method.get_string() == "Custom"


@Gtk.Template(resource_path=get_resource_path("ui/preferences_view.ui"))
class ViewPage(Adw.PreferencesPage):
    __gtype_name__ = "ViewPage"

    style_manager = Adw.StyleManager.get_default()

    @Gtk.Template.Callback()
    def toggleDark(self, switchrow, active):
        if switchrow.get_active():
            self.style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)
        else:
            self.style_manager.set_color_scheme(Adw.ColorScheme.FORCE_LIGHT)


@Gtk.Template(resource_path=get_resource_path("ui/preferences_zoom.ui"))
class ZoomPage(Adw.PreferencesPage):
    __gtype_name__ = "ZoomPage"
