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
