import Adw from "gi://Adw";
import Gtk from "gi://Gtk";
import Gdk from "gi://Gdk";
import Gio from "gi://Gio";

const { application, builder } = workbench;
const parent = workbench.window;

const app = workbench.builder.get_object("app");
const app_group = new Gio.SimpleActionGroup();
app.insert_action_group("app", app_group);

const quit_action = new Gio.SimpleAction({
  name: "quit",
});

quit_action.connect("activate", (action) => {
  application.quit();
});
application.set_accels_for_action("app.quit", ["<Control>Q"]);
app_group.add_action(quit_action);

const about_action = new Gio.SimpleAction({
  name: "about",
});

function openAboutWindow() {
  const dialog = new Adw.AboutWindow({
    transient_for: parent,
    application_icon: "com.github.xournalpp.xournalpp.svg",
    application_name: "Xournal++",
    developer_name: "Xournal++ developers",
    version: "1.2.1",
    comments: _("Xournal++ is an app for handwritten note taking."),
    website: "https://xournalpp.github.io",
    issue_url: "https://github.com/xournalpp/xournalpp/issues",
    support_url: "https://github.com/xournalpp/xournalpp/discussions",
    license_type: Gtk.License.GPL_2_0,
    developers: [
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
    artists: ["Nararyans R.I", "Luya Tshimbalanga"],
    translator_credits: _("translator-credits"),
  });

  dialog.present();
}

about_action.connect("activate", openAboutWindow);
app_group.add_action(about_action);

const shortcuts_action = new Gio.SimpleAction({
  name: "shortcuts",
});

shortcuts_action.connect("activate", (action) => {
  //  const builder = Gtk.Builder.new_from_resource(resource);
  //  const window = builder.get_object("shortcuts_window");
  //  window.set_transient_for(application.get_active_window());
  //  window.set_application(application);
  //  window.show();
});

application.set_accels_for_action("app.shortcuts", ["<Control>question"]);
app_group.add_action(shortcuts_action);

const help_action = new Gio.SimpleAction({
  name: "help",
});

help_action.connect("activate", (action) => {
  Gtk.show_uri(
    application.get_active_window(),
    "https://xournalpp.github.io/guide/whirlwind-tour/",
    Gdk.CURRENT_TIME,
  );
});
application.set_accels_for_action("app.shortcuts", ["F1"]);
app_group.add_action(help_action);

const preferences_action = new Gio.SimpleAction({
  name: "preferences",
});

preferences_action.connect("activate", (action) => {
  //
});
app_group.add_action(preferences_action);

const drawingArea = workbench.builder.get_object("drawing_area");

drawingArea.set_draw_func((area, cr, width, height) => {
  // Draw rectangle in drawing area
  cr.rectangle(30, 10, width - 60, height - 20);
  cr.setSourceRGBA(0.9, 0.9, 0.9, 1);
  cr.fill();
  cr.rectangle(30, 10, width - 60, height - 20);
  cr.setSourceRGBA(1, 0, 0, 1);
  cr.stroke();
  // Freeing the context before returning from the callback
  cr.$dispose();
});

