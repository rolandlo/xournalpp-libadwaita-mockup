from gi.repository import Gdk


class Marker_Config:
    def dicts_from_list(self, li, key1, key2):
        d12 = {}
        d21 = {}
        for l in li:
            d12[l[key1]] = l[key2]
            d21[l[key2]] = l[key1]
        return d12, d21

    marks_thicknesses = {
        0.132: "finer",  ### ln(0.42) + 1
        0.837: "fine",  #### ln(0.85) + 1
        1.344: "medium",  ## ln(1.41) + 1
        1.815: "thick",  ### ln(2.26) + 1
        2.735: "thicker",  # ln(5.67) + 1
    }

    marks_opacity = {
        0: "0%",
        50: "50%",
        100: "100%",
    }

    palette = [
        {"name": "yellow3", "color": "#f6d32d"},
        {"name": "orange3", "color": "#ff7800"},
        {"name": "purple2", "color": "#c061cb"},
        {"name": "green2", "color": "#57e389"},
        {"name": "blue2", "color": "#62a0ea"},
        {"name": "dark2", "color": "#5e5c64"},
        {"name": "green5", "color": "#26a269"},
        {"name": "red3", "color": "#e01b24"},
        {"name": "blue4", "color": "#1c71d8"},
    ]

    linestyles = [
        {"name": "plain", "icon": "line-style-plain-symbolic"},
        {"name": "dash", "icon": "line-style-dash-symbolic"},
        {"name": "dash_dot", "icon": "line-style-dash-dot-symbolic"},
        {"name": "dot", "icon": "line-style-dot-symbolic"},
    ]

    drawingtypes = [
        {"name": "rect", "icon": "rect"},
        {"name": "ellipse", "icon": "ellipse"},
        {"name": "arrow", "icon": "arrow"},
        {"name": "doublearrow", "icon": "double-arrow"},
        {"name": "line", "icon": "line"},
        {
            "name": "coordinatesystem",
            "icon": "coordinate-system",
        },
        {"name": "spline", "icon": "spline"},
        {
            "name": "shaperecognizer",
            "icon": "shape-recognizer",
        },
    ]

    default_rgba = Gdk.RGBA()
    default_rgba.parse("black")
