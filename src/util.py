import os

script_dir = os.path.dirname(os.path.realpath(__file__))


def get_ui_path(ui_file):
    return os.path.normpath(os.path.join(script_dir, "..", "ui", ui_file))


def get_resource_path(resource_file):
    return "/com/github/xournalpp/xournalpp-demo/" + resource_file
