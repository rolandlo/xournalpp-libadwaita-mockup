# window.py
#
# Copyright 2023 Roland Lötscher
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# SPDX-License-Identifier: GPL-2.0-or-later

import gi

gi.require_version("Poppler", "0.18")
gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
from gi.repository import Adw, Gtk, Gdk, Poppler
from .marker import Marker
from .util import get_resource_path, get_files_uri
from .toolbox import ToolBox
from .palettecolor import PaletteColor
from .marker_config import Marker_Config
from .tools_config import Tools_Config
from .sidebarpage import SidebarPage
from .maincontent import MainContent


@Gtk.Template(resource_path=get_resource_path("ui/window.ui"))
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"

    content_box = Gtk.Template.Child()
    stack = Gtk.Template.Child()
    document_properties_popover = Gtk.Template.Child()
    zoom_box = Gtk.Template.Child()
    zoom_entry = Gtk.Template.Child()
    content_split_view = Gtk.Template.Child()
    search_box = Gtk.Template.Child()
    searchbar = Gtk.Template.Child()
    drawing_tools = Gtk.Template.Child()
    color_tools = Gtk.Template.Child()
    text_tools = Gtk.Template.Child()
    selection_insertion_tools = Gtk.Template.Child()
    page_layer_tools = Gtk.Template.Child()
    background_tools = Gtk.Template.Child()
    audio_recording_tools = Gtk.Template.Child()
    geometry_tools = Gtk.Template.Child()
    custom_tools = Gtk.Template.Child()
    maincontent = Gtk.Template.Child()

    pages_box = Gtk.Template.Child()
    drop_target = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.document_properties_popover.add_child(self.zoom_box, "zoom_widgets")
        self.document = Poppler.Document.new_from_file(
            get_files_uri("test_document.pdf")
        )
        self.page = self.document.get_page(0)

        tools_config = Tools_Config()
        self.drawing_tools.init_widgets(
            [
                Gtk.Button(
                    icon_name=f"xopp-{tool['icon']}", tooltip_text=tool["tooltip"]
                )
                for tool in tools_config.drawing_tool_list
            ]
        )

        color_tools = []
        col = Gdk.RGBA()
        for palette_color in Marker_Config.palette:
            col.parse(palette_color["color"])
            color_tools.append(
                PaletteColor(rgba=col, tooltip_text=palette_color["name"])
            )
        col.parse("orange")
        color_tools.append(Gtk.ColorButton(rgba=col, tooltip_text="Choose Color"))

        self.color_tools.init_widgets(color_tools)

        self.text_tools.init_widgets(
            [
                Gtk.Button(icon_name="xopp-tool-text", tooltip_text="Text"),
                Gtk.FontButton(tooltip_text="Font"),
                Gtk.Button(
                    icon_name="xopp-tool-math-tex",
                    tooltip_text="Insert/Edit LaTeX",
                    action_name="app.latexeditor",
                ),
            ]
        )

        self.selection_insertion_tools.init_widgets(
            [
                Gtk.Button(
                    icon_name=f"xopp-{tool['icon']}", tooltip_text=tool["tooltip"]
                )
                for tool in tools_config.selection_insertion_list
            ]
        )

        self.page_layer_tools.init_widgets(
            [
                Gtk.Button(icon_name=tool["icon"], tooltip_text=tool["tooltip"])
                for tool in tools_config.page_tool_list
            ]
        )

        self.background_tools.init_widgets(
            [
                Gtk.Button(
                    icon_name=f"xopp-{tool['icon']}", tooltip_text=tool["tooltip"]
                )
                for tool in tools_config.background_tool_list
            ]
        )

        self.audio_recording_tools.init_widgets(
            [
                Gtk.Button(
                    icon_name=f"xopp-{tool['icon']}", tooltip_text=tool["tooltip"]
                )
                for tool in tools_config.audio_recording_list
            ]
        )
        self.geometry_tools.init_widgets(
            [
                Gtk.Button(icon_name="xopp-setsquare", tooltip_text="Setsquare"),
                Gtk.Button(icon_name="xopp-compass", tooltip_text="Compass"),
            ]
        )

        splinecol = Gdk.RGBA()
        splinecol.parse("violet")
        self.custom_tools.init_widgets(
            [
                Marker(),
                Marker(
                    fill=True,
                    drawingtype="spline",
                    thickness=3.0,
                    opacity=80,
                    linestyle="dash",
                    rgba=splinecol,
                ),
            ]
        )

        self.drop_target.set_actions(Gdk.DragAction.COPY)
        self.drop_target.set_gtypes([SidebarPage])

    @Gtk.Template.Callback()
    def on_button_preview_clicked(self, button):
        self.stack.set_visible_child_name("page_preview")

    @Gtk.Template.Callback()
    def on_button_workspace_clicked(self, button):
        self.stack.set_visible_child_name("page_workspace")

    @Gtk.Template.Callback()
    def on_button_library_clicked(self, button):
        self.stack.set_visible_child_name("page_library")

    @Gtk.Template.Callback()
    def on_entry_icon_press(self, entry, position):
        self.zoom = float(self.zoom_entry.get_text()[:-1]) / 100
        if position == Gtk.EntryIconPosition(0):
            self.zoom /= 1.1
        else:
            self.zoom *= 1.1

        self.zoom_entry.set_text(f"{int(self.zoom*100)}%")

    @Gtk.Template.Callback()
    def on_search_button_clicked(self, button):
        self.searchbar.set_search_mode(not self.searchbar.get_search_mode())

    @Gtk.Template.Callback()
    def on_droptarget_drop(self, droptarget, value, x, y):
        target_index = self.pages_box.get_child_at_pos(x, y).get_index()
        source_index = value.get_parent().get_index()
        if target_index != source_index:
            self.pages_box.remove(value)
            self.pages_box.insert(value, target_index)
            self.maincontent.set_page(value.pageno)
        return True

    @Gtk.Template.Callback()
    def on_flowbox_child_activated(self, flowbox, child):
        self.maincontent.set_page(child.get_child().pageno)
