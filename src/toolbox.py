import gi
from .util import get_resource_path

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, GObject, Adw


@Gtk.Template(resource_path=get_resource_path("ui/toolbox.ui"))
class ToolBox(Gtk.Box):
    __gtype_name__ = "ToolBox"

    lbl_title = Gtk.Template.Child()
    widget_box = Gtk.Template.Child()

    title = GObject.Property(type=str)

    def __init__(self):
        super().__init__()
        self.bind_property(
            "title", self.lbl_title, "label", GObject.BindingFlags.SYNC_CREATE
        )

    def init_widgets(self, widget_list):
        for widget in widget_list:
            self.append_widget(widget)

    def append_widget(self, widget):
        child = self.widget_box.get_first_child()
        while child:
            if widget == child:
                print("Widget already contained in ToolBox")
                return
            child = child.get_next_sibling()

        self.widget_box.append(widget)
