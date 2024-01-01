import gi
import re
from .util import get_resource_path

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw


@Gtk.Template(resource_path=get_resource_path("ui/pluginmanager.ui"))
class PluginManager(Adw.Window):
    __gtype_name__ = "PluginManager"

    plugin_searchbar = Gtk.Template.Child()
    plugin_searchentry = Gtk.Template.Child()
    plugin_listbox = Gtk.Template.Child()
    results_count = 0

    def filter(self, row):
        match = re.search(
            self.plugin_searchentry.get_text(),
            row.get_child().get_title(),
            re.IGNORECASE,
        )
        if match:
            self.results_count += 1
        return match

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.plugin_listbox.set_filter_func(self.filter)

    @Gtk.Template.Callback()
    def on_plugin_search_button_clicked(self, button):
        self.plugin_searchbar.set_search_mode(
            not self.plugin_searchbar.get_search_mode()
        )

    @Gtk.Template.Callback()
    def on_searchentry_search_changed(self, search):
        self.plugin_listbox.invalidate_filter()
