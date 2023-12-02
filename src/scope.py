import gi
import sys
import os

sys.path.append(os.path.dirname(__file__))

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GObject

import uisymbols


def define_builder_scope():
    class BuilderScope(GObject.GObject, Gtk.BuilderScope):
        def __init__(self, scope_object=None):
            super().__init__()

        def do_create_closure(self, builder, func_name, flags, obj):
            if hasattr(uisymbols, func_name):
                return getattr(uisymbols, func_name)
            else:
                print(f"Symbol {func_name} is not defined in uisymbols")

    return BuilderScope
