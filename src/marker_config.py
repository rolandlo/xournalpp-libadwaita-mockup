class Marker_Config:
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
        {"name": "linestyle_plain", "icon": "line-style-plain-symbolic"},
        {"name": "linestyle_dash", "icon": "line-style-dash-symbolic"},
        {"name": "linestyle_dash_dot", "icon": "line-style-dash-dot-symbolic"},
        {"name": "linestyle_dot", "icon": "line-style-dot-symbolic"},
    ]

    drawingtypes = [
        {"name": "drawingtype_rect", "icon": "rect"},
        {"name": "drawingtype_ellipse", "icon": "ellipse"},
        {"name": "drawingtype_arrow", "icon": "arrow"},
        {"name": "drawingtype_doublearrow", "icon": "double-arrow"},
        {"name": "drawingtype_line", "icon": "line"},
        {
            "name": "drawingtype_coordinatesystem",
            "icon": "coordinate-system",
        },
        {"name": "drawingtype_spline", "icon": "spline"},
        {
            "name": "drawingtype_shaperecognizer",
            "icon": "shape-recognizer",
        },
    ]
