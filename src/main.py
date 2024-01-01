#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("GtkSource", "5")
from gi.repository import Adw, Gtk, Gio, GtkSource
from .window import MainWindow
from .util import get_resource_path
from .scope import define_builder_scope
from .actions import add_actions
from .pluginentry import PluginEntry
from .pluginmanager import PluginManager
from .export import ExportDialog


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.builder = Gtk.Builder()
        BuilderScope = define_builder_scope()
        self.builder.set_scope(BuilderScope())

    def do_activate(self):
        win = self.props.active_window

        if not win:
            win = MainWindow(application=self)
        win.present()

        tmp = [
            GtkSource.StyleSchemeChooserButton(),
        ]  # throw away objects
        self.builder.add_from_resource(get_resource_path("ui/preferences.ui"))
        self.win_prefs = self.builder.get_object("win_prefs")
        self.win_prefs.set_hide_on_close(True)
        self.builder.add_from_resource(get_resource_path("ui/latexeditor.ui"))
        self.latexEditorDialog = self.builder.get_object("latexEditorDialog")
        self.latexEditorDialog.set_hide_on_close(True)
        self.builder.add_from_resource(get_resource_path("ui/pagetemplate.ui"))
        self.pageTemplateDialog = self.builder.get_object("pageTemplateDialog")
        self.pageTemplateDialog.set_hide_on_close(True)
        self.builder.add_from_resource(get_resource_path("ui/papercolor.ui"))
        self.paperColorDialog = self.builder.get_object("paperColorDialog")
        self.builder.add_from_resource(get_resource_path("ui/paperformat.ui"))
        self.paperFormatDialog = self.builder.get_object("paperFormatDialog")
        self.paperFormatDialog.set_hide_on_close(True)
        self.exportDialog = ExportDialog()
        self.exportDialog.set_hide_on_close(True)
        self.pluginManager = PluginManager()
        self.pluginManager.set_hide_on_close(True)

        add_actions(self)


def main(argv):
    app = MyApp(
        application_id="com.github.xournalpp.xournalpp-demo",
        flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
    )
    return app.run(argv)
