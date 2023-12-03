import os

script_dir = os.path.dirname(os.path.realpath(__file__))


def get_files_uri(file):
    return "file://" + os.path.normpath(os.path.join(script_dir, "files", file))


def get_resource_path(resource_file):
    return "/com/github/xournalpp/xournalpp-demo/" + resource_file
