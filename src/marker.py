import gi
from math import floor
from .util import get_resource_path
from .marker_config import Marker_Config

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, GObject, Gdk


@Gtk.Template(resource_path=get_resource_path("ui/marker.ui"))
class Marker(Gtk.Grid):
    __gtype_name__ = "Marker"

    button = Gtk.Template.Child()
    im_marker = Gtk.Template.Child()
    im_linestyle = Gtk.Template.Child()
    im_drawingtype = Gtk.Template.Child()
    sw_filled = Gtk.Template.Child()
    ad_opacity = Gtk.Template.Child()
    ad_thickness = Gtk.Template.Child()
    scale_opacity = Gtk.Template.Child()
    scale_thickness = Gtk.Template.Child()
    drawingtype_box = Gtk.Template.Child()
    linestyle_box = Gtk.Template.Child()
    color_box = Gtk.Template.Child()

    cfg = Marker_Config()
    palette_color_from_name, _ = cfg.dicts_from_list(cfg.palette, "name", "color")
    linestyle_icon_from_name, linestyle_name_from_icon = cfg.dicts_from_list(
        cfg.linestyles, "name", "icon"
    )
    drawingtype_icon_from_name, drawingtype_name_from_icon = cfg.dicts_from_list(
        cfg.drawingtypes, "name", "icon"
    )

    fill = GObject.Property(type=bool, default=False)
    thickness = GObject.Property(type=float, default=1.41, minimum=-0.5, maximum=4.0)
    opacity = GObject.Property(type=int, default=50, minimum=0, maximum=100)
    linestyle = GObject.Property(type=str, default="plain")
    drawingtype = GObject.Property(type=str, default="rect")
    rgba = GObject.Property(type=Gdk.RGBA, default=cfg.default_rgba)  # without alpha

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind_property(
            "fill", self.sw_filled, "active", GObject.BindingFlags.SYNC_CREATE
        )

        self.bind_property(
            "drawingtype",
            self.im_drawingtype,
            "icon-name",
            GObject.BindingFlags.SYNC_CREATE,
            lambda _, name: self.drawingtype_icon_from_name[name],
            lambda _, icon: self.drawingtype_name_from_icon[icon],
        )

        self.bind_property(
            "linestyle",
            self.im_linestyle,
            "icon-name",
            GObject.BindingFlags.SYNC_CREATE,
            lambda _, name: self.linestyle_icon_from_name[name],
            lambda _, icon: self.linestyle_name_from_icon[icon],
        )
        self.bind_property(
            "opacity", self.ad_opacity, "value", GObject.BindingFlags.SYNC_CREATE
        )
        self.bind_property(
            "thickness", self.ad_thickness, "value", GObject.BindingFlags.SYNC_CREATE
        )

        # Add scale marks
        for value in self.cfg.marks_thicknesses:
            self.scale_thickness.add_mark(value, Gtk.PositionType.TOP, "")

        for value, label in self.cfg.marks_opacity.items():
            self.scale_opacity.add_mark(value, Gtk.PositionType.TOP, label)

        # Add palette colors
        for i, col in enumerate(self.cfg.palette):
            button = Gtk.Button()
            button.set_name(col["name"])
            button.add_css_class("circular")
            self.set_css_property(button, "background-color", col["color"])
            button.connect("clicked", self.on_color_button_clicked)
            self.color_box.append(button)

        # Add color dialog button
        color_dialog = Gtk.ColorDialog()
        color_dialog.set_with_alpha(False)
        color_button = Gtk.ColorDialogButton()
        color_button.set_dialog(color_dialog)
        color_button.set_name("color-chooser")
        color_button.connect("notify::rgba", self.set_color)
        self.color_box.append(color_button)

        # Add linestyles
        for style in self.cfg.linestyles:
            button = Gtk.Button()
            button.set_name(style["name"])
            button.set_icon_name(style["icon"])
            button.connect("clicked", self.on_linestyle_button_clicked)
            self.linestyle_box.append(button)

        # Add drawingtypes
        for type in self.cfg.drawingtypes:
            button = Gtk.Button()
            button.set_name(type["name"])
            button.set_icon_name(type["icon"])
            button.connect("clicked", self.on_drawingtype_button_clicked)
            self.drawingtype_box.append(button)

        self.connect("notify::rgba", self.on_color_changed)
        self.connect("notify::opacity", self.on_color_changed)
        self.on_color_changed(None, None)

    @Gtk.Template.Callback()
    def on_button_clicked(self, splitbutton):
        print("Hello button")

    @Gtk.Template.Callback()
    def on_thickness_changed(self, adjustment):
        self.set_css_property(
            self.im_linestyle,
            "-gtk-icon-transform",
            f"scale({(self.props.thickness + 2.0) / 3.0})",
        )

    @Gtk.Template.Callback()
    def on_filled_set(self, switch, active):
        self.im_marker.set_from_icon_name(
            "marker-filled-symbolic" if active else "marker-not-filled-symbolic"
        )

    def set_css_property(self, widget, property, value):
        cssString = f"#{widget.get_name()} {{ {property}: {value}; }}"
        provider = Gtk.CssProvider()
        provider.load_from_string(cssString)
        context = widget.get_style_context()
        context.add_provider(provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def set_color(self, button, _):
        self.props.rgba = button.get_rgba()

    def on_color_button_clicked(self, button):
        col = Gdk.RGBA()
        col.parse(self.palette_color_from_name[button.get_name()])
        self.props.rgba = col

    def on_drawingtype_button_clicked(self, button):
        self.props.drawingtype = button.get_name()

    def on_linestyle_button_clicked(self, button):
        self.props.linestyle = button.get_name()

    def on_color_changed(self, _, color):
        rgba = self.props.rgba
        rgba.alpha = self.props.opacity / 100
        self.set_css_property(self.im_marker, "color", rgba.to_string())
