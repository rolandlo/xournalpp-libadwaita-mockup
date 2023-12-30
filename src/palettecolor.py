from gi.repository import Gtk, Gdk, Graphene, Gsk, GObject


class PaletteColor(Gtk.Button):
    size = 20
    default_color = Gdk.RGBA()
    default_color.parse("red")
    rgba = GObject.Property(type=Gdk.RGBA, default=default_color)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.props.halign = Gtk.Align.CENTER
        self.set_size_request(self.size, self.size)

    def do_snapshot(self, snapshot):
        rect = Graphene.Rect().init(0, 0, self.size, self.size)

        rounded_rect = Gsk.RoundedRect()
        rounded_rect.init_from_rect(rect, radius=90)

        snapshot.push_rounded_clip(rounded_rect)
        snapshot.append_color(self.rgba, rect)
        snapshot.pop()  # remove the clip

    def do_measure(self, orientation, for_size):
        return self.size, self.size, -1, -1
