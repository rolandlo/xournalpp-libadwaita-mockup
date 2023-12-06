#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

copy_dict = {
    "export/main.blp": "ui/export.blp",
    "latexeditor/main.blp": "ui/latexeditor.blp",
    "window/main.blp": "ui/window.blp",
    "pagetemplate/main.blp": "ui/pagetemplate.blp",
    "paperformat/main.blp": "ui/paperformat.blp",
    "preferences/main.blp": "ui/preferences.blp",
    "help-overlay/main.blp": "gtk/help-overlay.blp",
    "marker/main.blp": "ui/marker.blp",
}

script_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.normpath(os.path.join(script_dir, ".."))

for source, target in copy_dict.items():
    input_path = os.path.join(root_dir, "workbench", source)
    output_path = os.path.join(root_dir, "src", target)
    print(f"Copy {input_path} to {output_path}")
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    shutil.copyfile(input_path, output_path)
