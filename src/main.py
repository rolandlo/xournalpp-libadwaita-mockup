#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import gi
from util import get_resource_path
from scope import define_builder_scope
from actions import add_actions

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("GtkSource", "5")
from gi.repository import Adw, Gtk, Gio, GtkSource


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect("activate", self.on_activate)
        self.builder = Gtk.Builder()
        BuilderScope = define_builder_scope()
        self.builder.set_scope(BuilderScope())

    #        self.spinbutton = SplitButton()

    def on_activate(self, app):
        self.builder.add_from_resource(get_resource_path("main.ui"))
        self.win = self.builder.get_object("app")
        self.win.set_application(app)
        self.win.present()

        tmp = (
            GtkSource.StyleSchemeChooserButton()
        )  # throw away object to make builder know of GtkSource.StyleSchemeChooserButton
        self.builder.add_from_resource(get_resource_path("preferences.ui"))
        self.win_prefs = self.builder.get_object("win_prefs")

        add_actions(app)


# @Gtk.Template(resource_path=get_resource_path("splitbutton.ui"))
# class SplitButton(Gtk.Grid):
#    __gtype_name__ = "Marker"


#    button = Gtk.Template.Child("button")


#    @Gtk.Template.Callback()
#    def on_button_clicked(self, *args):
#        print("Hello")


def main(argv):
    app = MyApp(
        application_id="com.github.xournalpp.xournalpp-demo",
        flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
    )
    return app.run(sys.argv)
