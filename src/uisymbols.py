import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

style_manager = Adw.StyleManager.get_default()


def checkTex(self):
    toast = Adw.Toast(title="Sample LaTeX file generated successfully")
    self.get_root().add_toast(toast)


def on_file_selected(dialog, result, button):
    file = dialog.open_finish(result)
    button.get_child().set_label(file.get_basename())


def on_folder_selected(dialog, result, button):
    folder = dialog.select_folder_finish(result)
    button.get_child().set_label(folder.get_basename())


def openFile(self):
    dialog = Gtk.FileDialog()
    filter = Gtk.FileFilter()
    filter.set_name(".tex file")
    filter.add_pattern("*.tex")
    dialog.set_default_filter(filter)
    dialog.open(None, None, on_file_selected, self)


def selectFolder(self):
    dialog = Gtk.FileDialog()
    folder = dialog.select_folder(None, None, on_folder_selected, self)


def toggleDark(self, active):
    if self.get_active():
        style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)
    else:
        style_manager.set_color_scheme(Adw.ColorScheme.FORCE_LIGHT)


def selectAudioFolder(self):
    print("Selecting audio folder")
    selectFolder(self)


def selectTemplate(self):
    print("Selecting template")
    openFile(self)


def showCustom(self, method):
    return method.get_string() == "Custom"


def showMean(self, method):
    return method.get_string() == "Arithmetic Mean"


def showGauss(self, method):
    return method.get_string() == "Gaussian weights"


def showDeadZone(self, method):
    return method.get_string() == "Dead Zone"


def showInertia(self, method):
    return method.get_string() == "Inertia"
