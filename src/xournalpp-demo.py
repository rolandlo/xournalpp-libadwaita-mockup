#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import sys
    import gi
    from util import get_ui_path, get_resource_path

    from gi.repository import Gio

    resource = Gio.Resource.load(get_ui_path("xournalpp-demo.gresource"))
    resource._register()

    from main import main

    sys.exit(main(sys.argv))
