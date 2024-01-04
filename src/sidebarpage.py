import gi
from .util import get_resource_path, get_files_uri

gi.require_version("Gtk", "4.0")
gi.require_version("Poppler", "0.18")

from gi.repository import Gtk, GObject, Poppler, Gdk


@Gtk.Template(resource_path=get_resource_path("ui/sidebarpage.ui"))
class SidebarPage(Gtk.Box):
    __gtype_name__ = "SidebarPage"

    page_area = Gtk.Template.Child()
    page_tools = Gtk.Template.Child()

    width = GObject.Property(type=float, default=595.0, minimum=10.0, maximum=10_000.0)
    height = GObject.Property(
        type=float,
        default=842.0,
    )
    scale = GObject.Property(type=float, default=0.15, minimum=0.01, maximum=10.0)
    pageno = GObject.Property(type=int, default=0, minimum=0, maximum=10_000)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.document = Poppler.Document.new_from_file(
            get_files_uri("test_document.pdf")
        )
        self.page = self.document.get_page(self.pageno)

        self.page_area.set_draw_func(self.draw)
        self.connect("notify::height", self.on_size_changed)
        self.connect("notify::width", self.on_size_changed)
        self.connect("notify::scale", self.on_size_changed)
        self.connect("notify::pageno", self.on_pageno_changed)

    @Gtk.Template.Callback()
    def on_enter(self, x, y, data):
        self.page_tools.set_visible(True)

    @Gtk.Template.Callback()
    def on_leave(self, data):
        self.page_tools.set_visible(False)

    @Gtk.Template.Callback()
    def on_dragsource_prepare(self, dragsource, x, y):
        self.drag_x = x
        self.drag_y = y
        value = GObject.Value()
        value.init(SidebarPage)
        value.set_object(self)
        return Gdk.ContentProvider.new_for_value(value)

    @Gtk.Template.Callback()
    def on_dragsource_drag_begin(self, dragsource, drag):
        allocation = self.get_allocation()
        drag_widget = Gtk.Box()
        drag_widget.set_size_request(allocation.width, allocation.height)
        drag_page = SidebarPage(pageno=self.pageno)
        drag_widget.append(drag_page)
        icon = Gtk.DragIcon.get_for_drag(drag)
        icon.set_child(drag_widget)
        drag.set_hotspot(self.drag_x, self.drag_y)

    def draw(self, area, cr, width, height):
        cr.set_source_rgba(1.0, 1.0, 1.0, 1.0)
        cr.rectangle(0, 0, width, height)
        cr.fill()
        cr.scale(self.scale, self.scale)
        self.page.render(cr)

    def on_size_changed(self, page, param):
        self.page_area.set_content_width(self.width * self.scale)
        self.page_area.set_content_height(self.height * self.scale)

    def on_pageno_changed(self, page, param):
        self.page = self.document.get_page(self.pageno)
        self.width, self.height = self.page.get_size()
