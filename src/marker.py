import gi
from .util import get_resource_path

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk


@Gtk.Template(resource_path=get_resource_path("ui/marker.ui"))
class Marker(Gtk.Grid):
    __gtype_name__ = "Marker"

    button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_button_clicked(self, splitbutton):
        print("Hello button")

    @Gtk.Template.Callback()
    def on_thickness_changed(self, adjustment):
        print("Hello thickness")

    @Gtk.Template.Callback()
    def on_opacity_changed(self, adjustment):
        print("Hello opacity")

    @Gtk.Template.Callback()
    def on_filled_set(self, switch, active):
        print(switch, active)
        print("Hello filled")
