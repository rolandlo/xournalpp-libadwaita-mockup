import os

script_dir = os.path.dirname(os.path.realpath(__file__))


def get_files_uri(file):
    path = "file://" + os.path.normpath(os.path.join(script_dir, "files", file))
    return path.replace("/C:/", "/C/")  # hack to make it work on Windows


def get_resource_path(resource_file):
    return "/com/github/xournalpp/xournalpp-demo/" + resource_file
