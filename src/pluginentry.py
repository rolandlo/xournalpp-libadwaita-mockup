import gi
from .util import get_resource_path

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, GObject


@Gtk.Template(resource_path=get_resource_path("ui/pluginentry.ui"))
class PluginEntry(Gtk.ListBox):
    __gtype_name__ = "PluginEntry"

    lbl_title = Gtk.Template.Child()
    lbl_description = Gtk.Template.Child()
    lbl_author = Gtk.Template.Child()
    lbl_path = Gtk.Template.Child()
    lbl_version = Gtk.Template.Child()
    sw_enabled = Gtk.Template.Child()

    title = GObject.Property(type=str)
    description = GObject.Property(type=str)
    author = GObject.Property(type=str)
    path = GObject.Property(type=str)
    version = GObject.Property(type=str)
    enabled = GObject.Property(type=bool, default=False)
    default_enabled = GObject.Property(type=bool, default=False)

    def __init__(self):
        super().__init__()
        self.bind_property(
            "title", self.lbl_title, "label", GObject.BindingFlags.SYNC_CREATE
        )
        self.bind_property(
            "description",
            self.lbl_description,
            "label",
            GObject.BindingFlags.SYNC_CREATE,
        )
        self.bind_property(
            "author", self.lbl_author, "label", GObject.BindingFlags.SYNC_CREATE
        )
        self.bind_property(
            "path",
            self.lbl_path,
            "label",
            GObject.BindingFlags.DEFAULT,
            lambda _, path: "<tt>" + path + "</tt>",
        )
        self.bind_property(
            "version", self.lbl_version, "label", GObject.BindingFlags.SYNC_CREATE
        )
        self.bind_property(
            "enabled", self.sw_enabled, "active", GObject.BindingFlags.SYNC_CREATE
        )

    def get_title(self):
        return self.lbl_title.get_label()
