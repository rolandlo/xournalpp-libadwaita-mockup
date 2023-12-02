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

from gi.repository import Adw, Gtk
from .marker import Marker
from .util import get_resource_path


@Gtk.Template(resource_path=get_resource_path("ui/window.ui"))
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"

    content_box = Gtk.Template.Child()
    drawing_area = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.marker = Marker(
            color="#8ff0a4",
            fill=True,
            marker_opacity=50.0,
            linestyle="dash-dot",
            thickness=0.837,
            drawingtype="arrow",
        )
        self.content_box.prepend(self.marker)

        self.drawing_area.set_draw_func(self.draw)

    def draw(self, area, cr, width, height):
        # Draw rectangle in drawing area
        cr.rectangle(30, 10, width - 60, height - 20)
        cr.set_source_rgba(0.9, 0.9, 0.9, 1)
        cr.fill()
        cr.rectangle(30, 10, width - 60, height - 20)
        cr.set_source_rgba(1, 0, 0, 1)
        cr.stroke()
