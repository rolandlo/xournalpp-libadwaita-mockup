import gi
from util import get_resource_path

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Gio, Gdk, Adw, GLib


def openAboutWindow(app):
    dialog = Adw.AboutWindow(
        transient_for=app.props.active_window,
        application_name="Xournal++",
        application_icon="com.github.xournalpp.xournalpp",
        developer_name="Xournal++ developers",
        version="1.2.2",
        comments="Xournal++ is an app for handwritten note taking.",
        website="https://xournalpp.github.io",
        issue_url="https://github.com/xournalpp/xournalpp/issues",
        support_url="https://github.com/xournalpp/xournalpp/discussions",
        license_type=Gtk.License.GPL_2_0,
        developers=[
            "2010-2021, Andreas Butti <andreas.butti@gmail.com>",
            "2012-2018, Wilson Brenna <wilson@wbrenna.homelinux.com>",
            "2015-2016, Marek Pikuła <marek@pikula.tk>",
            "2017-2019, Peter Klausing <peetCreative@users.noreply.github.com>",
            "2018-2019, Moreno Razzoli <morrolinux@users.noreply.github.com>",
            "2018-2019, Luca Errani <luca.errani1@gmail.com>",
            "2019-2022, Ulrich Huber <ulrich@huberulrich.de>",
            "2019-2019, Justin Jones <bjustjones@netscape.net>",
            "2019-2023, Bryan Tan <Technius@users.noreply.github.com>",
            "2019-2019, Justus Rossmeier <veecue@users.noreply.github.com>",
            "2019-2023, Fabian Keßler <Fabian_Kessler@gmx.de>",
            "2019-2020, Julius Lehmann <internet@devpi.de>",
            "2020-2021, Tobias Hermann <idotobi@users.noreply.github.com>",
            "2020-2023, Roland Lötscher <roland_loetscher@hotmail.com>",
            "2021-2023, Benjamin Hennion <benjamin.hennion@wanadoo.fr>",
            "2021-2022, Henry Heino <personalizedrefrigerator@gmail.com>",
        ],
        artists=["Nararyans R.I", "Luya Tshimbalanga"],
        # translator_credits="translator-credits",
    )

    dialog.present()


def toggle_group(group):
    if group.get_visible():
        group.hide()
    else:
        group.show()


def toggle_all_tools(win):
    win.content_split_view.set_show_sidebar(True)
    win.drawing_tools.show()
    win.color_tools.show()
    win.text_tools.show()
    win.selection_insertion_tools.show()
    win.page_layer_tools.show()
    win.background_tools.show()
    win.audio_recording_tools.show()
    win.geometry_tools.show()
    win.custom_tools.show()


def add_action(app, name, callback, group, shortcuts=None):
    action = Gio.SimpleAction(name=name)
    action.connect("activate", callback)
    app.add_action(action)
    group.add_action(action)
    if shortcuts:
        app.set_accels_for_action(f"app.{name}", shortcuts)


def add_actions(app):
    app_group = Gio.SimpleActionGroup()
    win = app.props.active_window
    win.insert_action_group("app", app_group)

    add_action(app, "quit", lambda *_: app.quit(), app_group, ["<Control>Q"])
    add_action(app, "about", lambda *_: openAboutWindow(app), app_group)
    add_action(
        app,
        "help",
        lambda *_: Gtk.show_uri(
            app.get_active_window(),
            "https://xournalpp.github.io/guide/whirlwind-tour/",
            Gdk.CURRENT_TIME,
        ),
        app_group,
        ["F1"],
    )
    add_action(app, "preferences", lambda *_: app.win_prefs.present(), app_group)
    add_action(
        app, "latexeditor", lambda *_: app.latexEditorDialog.present(), app_group
    )
    add_action(
        app, "pagetemplate", lambda *_: app.pageTemplateDialog.present(), app_group
    )
    add_action(
        app,
        "papercolor",
        lambda *_: app.paperColorDialog.choose_rgba(win, Gdk.RGBA(), None, None, None),
        app_group,
    )
    add_action(
        app, "paperformat", lambda *_: app.paperFormatDialog.present(), app_group
    )
    add_action(app, "export-as", lambda *_: app.exportDialog.present(), app_group)
    add_action(app, "plugin-manager", lambda *_: app.pluginManager.present(), app_group)
    add_action(
        app,
        "toggle-drawing-tools",
        lambda *_: toggle_group(win.drawing_tools),
        app_group,
    )
    add_action(
        app,
        "toggle-colors",
        lambda *_: toggle_group(win.color_tools),
        app_group,
    )
    add_action(
        app,
        "toggle-text-tools",
        lambda *_: toggle_group(win.text_tools),
        app_group,
    )
    add_action(
        app,
        "toggle-selection-tools",
        lambda *_: toggle_group(win.selection_insertion_tools),
        app_group,
    )
    add_action(
        app,
        "toggle-page-layer-tools",
        lambda *_: toggle_group(win.page_layer_tools),
        app_group,
    )
    add_action(
        app,
        "toggle-background-tools",
        lambda *_: toggle_group(win.background_tools),
        app_group,
    )
    add_action(
        app,
        "toggle-audio-tools",
        lambda *_: toggle_group(win.audio_recording_tools),
        app_group,
    )
    add_action(
        app,
        "toggle-geometry-tools",
        lambda *_: toggle_group(win.geometry_tools),
        app_group,
    )
    add_action(
        app,
        "show-tools-sidebar",
        lambda *_: win.content_split_view.set_show_sidebar(True),
        app_group,
    )
    add_action(
        app,
        "hide-tools-sidebar",
        lambda *_: win.content_split_view.set_show_sidebar(False),
        app_group,
    )
    add_action(app, "toggle-all-tools", lambda *_: toggle_all_tools(win), app_group)
    add_action(app, "export", lambda *_: Gtk.FileDialog().save(), app_group)
    add_action(app, "save", lambda *_: Gtk.FileDialog().save(), app_group)
    add_action(app, "save-as", lambda *_: Gtk.FileDialog().save(), app_group)
