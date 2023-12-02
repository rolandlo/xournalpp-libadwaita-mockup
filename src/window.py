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

from gi.repository import Adw
from gi.repository import Gtk
from .marker import Marker
from .util import get_resource_path


@Gtk.Template(resource_path=get_resource_path("ui/window.ui"))
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"

    content_box = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.marker = Marker()
        self.content_box.append(self.marker)