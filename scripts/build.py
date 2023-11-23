#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os

dirs = [
    "export",
    "latexeditor",
    "main",
    "pagetemplate",
    "paperformat",
    "preferences",
    "shortcuts",
    "splitbutton",
]
script_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.normpath(os.path.join(script_dir, ".."))
ui_dir = os.path.join(root_dir, "ui")

for dir in dirs:
    input_path = os.path.join(root_dir, dir, "main.blp")
    output_path = os.path.join(ui_dir, dir + ".ui")
    result = subprocess.run(
        [f"blueprint-compiler compile {input_path} --output={output_path}"],
        shell=True,
        capture_output=False,
        text=False,
    )
    print(f"Generated {output_path}")

old_path = os.path.join(ui_dir, "shortcuts.ui")
new_path = os.path.join(ui_dir, "gtk", "help-overlay.ui")

os.rename(old_path, new_path)
print(f"Renamed {old_path} to {new_path}")

resource_xml = os.path.normpath(os.path.join(ui_dir, "xournalpp-demo.gresource.xml"))
os.chdir(ui_dir)
subprocess.run(["glib-compile-resources", resource_xml])
print(f"Compiled {resource_xml} into {resource_xml[:-4]}")
