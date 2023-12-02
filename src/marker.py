import gi
from math import floor
from .util import get_resource_path
from .marker_config import Marker_Config

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gtk


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

    def __init__(self, color, fill, marker_opacity, linestyle, thickness, drawingtype):
        super().__init__()
        self.color = color
        self.marker_opacity = marker_opacity
        self.sw_filled.active = fill
        self.set_css_property(self.im_marker, "color", self.hex(color, marker_opacity))
        self.im_linestyle.set_from_icon_name(f"line-style-{linestyle}")
        self.im_drawingtype.set_from_icon_name(drawingtype)
        self.ad_opacity.set_value(marker_opacity)
        self.ad_thickness.set_value(thickness)

        for value in self.cfg.marks_thicknesses:
            self.scale_thickness.add_mark(value, Gtk.PositionType.TOP, "")

        for value, label in self.cfg.marks_opacity.items():
            self.scale_opacity.add_mark(value, Gtk.PositionType.TOP, label)

        for i, col in enumerate(self.cfg.palette):
            button = Gtk.Button()
            button.set_name(col["name"])
            button.add_css_class("circular")
            self.set_css_property(button, "background-color", col["color"])
            button.connect(
                "clicked",
                lambda button: self.set_css_property(
                    self.im_marker,
                    "color",
                    next(
                        filter(
                            lambda col: col["name"] == button.get_name(),
                            self.cfg.palette,
                        )
                    )["color"],
                ),
            )
            self.color_box.append(button)

        color_dialog = Gtk.ColorDialog()
        color_dialog.set_with_alpha(False)
        color_button = Gtk.ColorDialogButton()
        color_button.set_dialog(color_dialog)
        color_button.set_name("color-chooser")
        color_button.connect("notify::rgba", self.set_color)
        self.color_box.append(color_button)

        for style in self.cfg.linestyles:
            button = Gtk.Button()
            button.set_name(style["name"])
            button.set_icon_name(style["icon"])
            button.connect(
                "clicked",
                lambda data: self.im_linestyle.set_from_icon_name(
                    next(
                        filter(
                            lambda style: style["name"] == data.get_name(),
                            self.cfg.linestyles,
                        )
                    )["icon"]
                ),
            )

            self.linestyle_box.append(button)

        for type in self.cfg.drawingtypes:
            button = Gtk.Button()
            button.set_name(type["name"])
            button.set_icon_name(type["icon"])
            button.connect(
                "clicked",
                lambda data: self.im_drawingtype.set_from_icon_name(
                    next(
                        filter(
                            lambda type: type["name"] == data.get_name(),
                            self.cfg.drawingtypes,
                        )
                    )["icon"]
                ),
            )

            self.drawingtype_box.append(button)

    @Gtk.Template.Callback()
    def on_button_clicked(self, splitbutton):
        print("Hello button")

    @Gtk.Template.Callback()
    def on_thickness_changed(self, adjustment):
        self.thickness = adjustment.get_value()
        self.set_css_property(
            self.im_linestyle,
            "-gtk-icon-transform",
            f"scale({(self.thickness + 2.0) / 3.0})",
        )

    @Gtk.Template.Callback()
    def on_opacity_changed(self, adjustment):
        self.marker_opacity = adjustment.get_value()
        self.set_css_property(
            self.im_marker,
            "color",
            self.hex(self.color, self.marker_opacity),
        )

    @Gtk.Template.Callback()
    def on_filled_set(self, switch, active):
        if active:
            self.im_marker.set_from_icon_name("marker-filled-symbolic")
        else:
            self.im_marker.set_from_icon_name("marker-not-filled-symbolic")

    def set_css_property(self, widget, property, value):
        cssString = f"#{widget.get_name()} {{ {property}: {value}; }}"
        provider = Gtk.CssProvider()
        provider.load_from_string(cssString)
        context = widget.get_style_context()
        context.add_provider(provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def hex(self, color, opacity):
        alpha_decimal = floor((opacity + 100) * 1.275)
        alpha = f"{alpha_decimal:x}"
        return f"{color}{alpha}"

    def get_color_from_rgba(self, rgba):
        r = floor(rgba.red * 255)
        g = floor(rgba.green * 255)
        b = floor(rgba.b * 255)
        return f"#{r:x}{g:x}{b:x}"

    def set_color(self, button, whatever):
        self.color = self.get_color_from_rgba(button.rgba)
        self.set_css_property(
            self.im_marker, "color", self.hex(self.color, self.marker_opacity)
        )
