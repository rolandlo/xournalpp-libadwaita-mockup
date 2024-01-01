import gi
from .util import get_resource_path

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw


@Gtk.Template(resource_path=get_resource_path("ui/export.ui"))
class ExportDialog(Adw.Window):
    __gtype_name__ = "ExportDialog"

    btn_export_file = Gtk.Template.Child()
    format = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def image_quality_visible(self, dialog, format):
        return format.get_string() == "png"

    @Gtk.Template.Callback()
    def selectExportFile(self, button):
        ending = self.format.get_selected_item().get_string()
        print(ending)
        dialog = Gtk.FileDialog(initial_name=f"example.{ending}")
        filter = Gtk.FileFilter()
        filter.set_name("{ending} format")
        filter.add_pattern(f"*.{ending}")
        dialog.set_default_filter(filter)
        dialog.save(None, None, self.on_file_selected)

    def on_file_selected(self, dialog, result):
        file = dialog.save_finish(result)
        self.btn_export_file.get_child().set_label(file.get_basename())
