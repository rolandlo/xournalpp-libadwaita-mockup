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
from math import pi
from itertools import pairwise


@Gtk.Template(resource_path=get_resource_path("ui/window.ui"))
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"

    content_box = Gtk.Template.Child()
    drawing_area = Gtk.Template.Child()
    stack = Gtk.Template.Child()

    DOT_RADIUS = 5
    CROSS_SIZE = 4
    STROKE_WIDTH = 3
    PRESSURE_MULTIPLIER = 2
    BOX = (300, 50, 50)  # x, y, r

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
        self.document = Poppler.Document.new_from_file(get_files_uri("sample.pdf"))
        self.page = self.document.get_page(0)

        self.dots = []
        self.crosses = []
        self.stroke = []
        self.delta = 0
        self.scale = 1

    def draw(self, area, cr, width, height):
        w, h = self.page.get_size()
        # Draw rectangle in drawing area
        f = 1.0
        if width < w or height < h:
            f = min(width / w, height / h)
        cr.rectangle(0, 0, w, h)
        cr.set_source_rgba(0.9, 0.9, 0.9, 1)  # light gray
        cr.fill()
        cr.rectangle(0, 0, w, h)
        cr.set_source_rgba(1, 0, 0, 1)  # red
        cr.stroke()
        cr.scale(f, f)
        self.page.render(cr)

        cr.set_source_rgba(0, 0.5, 0, 1)  # green
        for x, y in self.dots:
            cr.move_to(x, y)
            cr.arc(x, y, self.DOT_RADIUS, 0, 2 * pi)
        cr.fill()

        cr.set_source_rgba(0, 0, 1, 1)  # blue
        for x, y in self.crosses:
            cr.move_to(x - self.CROSS_SIZE, y - self.CROSS_SIZE)
            cr.rel_line_to(2 * self.CROSS_SIZE, 2 * self.CROSS_SIZE)
            cr.move_to(x - self.CROSS_SIZE, y + self.CROSS_SIZE)
            cr.rel_line_to(2 * self.CROSS_SIZE, -2 * self.CROSS_SIZE)
        cr.stroke()

        cr.set_source_rgba(1, 1, 0, 0.5)  # yellow
        cr.save()
        x, y, r = self.BOX
        r *= self.scale
        cr.translate(x, y)
        cr.rotate(self.delta)
        cr.translate(-x, -y)
        cr.rectangle(x - r, y - r, 2 * r, 2 * r)
        cr.restore()
        cr.fill()

        cr.set_source_rgba(1, 0, 1, 1)  # magenta
        if len(self.stroke) > 0:
            for p, q in pairwise(self.stroke[1:]):
                cr.move_to(p[0], p[1])
                cr.set_line_width(self.STROKE_WIDTH * p[2])
                cr.line_to(q[0], q[1])
                cr.stroke()

    def filtered_pressure(self, gesture):
        has_pressure, pressure = gesture.get_axis(Gdk.AxisUse.PRESSURE)
        return has_pressure and self.PRESSURE_MULTIPLIER * pressure or 1

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
    def on_gestureclick_released(self, gesture, n_press, x, y):
        if n_press == 1:  # single click (or first click in double click)
            self.dots.append((x, y))
        elif n_press == 2:  # double click
            self.dots.pop()
            self.crosses.append((x, y))
        self.drawing_area.queue_draw()

    @Gtk.Template.Callback()
    def on_gestureclick_pressed(self, gesture, n_press, x, y):
        if n_press == 1:
            pass  # print(f"click at ({x}, {y})")
        elif n_press == 2:
            pass  # print(f"double click at ({x}, {y})")

    @Gtk.Template.Callback()
    def on_gestureclick_stopped(self, gesture):
        pass  # print("click was stopped")

    @Gtk.Template.Callback()
    def on_gestureclick_unpaired_release(self, gesture, x, y, button, sequence):
        pass  # print("click release without press")

    @Gtk.Template.Callback()
    def on_gesturerotate_angle_changed(self, gesture, angle, angle_delta):
        # center = gesture.get_bounding_box_center()
        # print(f"rotation center = ({center.x}, {center.y})")
        self.delta = angle_delta
        self.drawing_area.queue_draw()

    @Gtk.Template.Callback()
    def on_gesturezoom_scale_changed(self, gesture, scale):
        self.scale = scale

    @Gtk.Template.Callback()
    def on_gesturestylus_down(self, gesture, x, y):
        self.stroke = [(x, y, self.filtered_pressure(gesture))]
        self.drawing_area.queue_draw()

    @Gtk.Template.Callback()
    def on_gesturestylus_motion(self, gesture, x, y):
        tool = gesture.get_device_tool()
        # print(f"tool type: {tool.get_tool_type()}, serial: {tool.get_serial()}, ")

        has_backlog, backlog = gesture.get_backlog()
        if has_backlog:
            for b in backlog:
                ax, ay, ap = (
                    b.axes[Gdk.AxisUse.X],
                    b.axes[Gdk.AxisUse.Y],
                    b.flags & Gdk.AxisFlags.PRESSURE
                    and self.PRESSURE_MULTIPLIER * b.axes[Gdk.AxisUse.PRESSURE]
                    or 1,
                )
                # print(f"x = {ax}, y = {ay}, pressure = {ap}")
                self.stroke.append((ax, ay, ap))
        else:
            self.stroke.append((x, y, self.filtered_pressure(gesture)))
        self.drawing_area.queue_draw()

    @Gtk.Template.Callback()
    def on_gesturestylus_proximity(self, gesture, x, y):
        pass  # print(f"stylus proximity at ({x}, {y})")

    @Gtk.Template.Callback()
    def on_gesturestylus_up(self, gesture, x, y):
        # print(f"stylus up at ({x}, {y})")
        self.stroke.append((x, y, self.filtered_pressure(gesture)))
        self.drawing_area.queue_draw()
