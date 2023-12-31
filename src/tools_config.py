from gi.repository import Gdk


class Tools_Config:
    drawing_tool_list = [
        {"icon": "tool-pencil", "tooltip": "Pen"},
        {"icon": "tool-highlighter", "tooltip": "Highlighter"},
        {"icon": "tool-eraser", "tooltip": "Eraser"},
        {"icon": "line-style-plain-with-pen", "tooltip": "Linestyle Plain"},
        {"icon": "line-style-dot-with-pen", "tooltip": "Linestyle Dot"},
        {"icon": "line-style-dash-with-pen", "tooltip": "Linestyle Dash"},
        {"icon": "line-style-dash-dot-with-pen", "tooltip": "Linestyle Dash-Dot"},
        {"icon": "thickness-finer", "tooltip": "Thickness Finer"},
        {"icon": "thickness-fine", "tooltip": "Thickeness Fine"},
        {"icon": "thickness-medium", "tooltip": "Thickness Medium"},
        {"icon": "thickness-thick", "tooltip": "Thickness Thick"},
        {"icon": "thickness-thicker", "tooltip": "Thickness Thicker"},
        {"icon": "fill", "tooltip": "Fill"},
        {"icon": "fill-opacity", "tooltip": "Opacity"},
        {"icon": "draw-rect", "tooltip": "Draw Rectangle"},
        {"icon": "draw-ellipse", "tooltip": "Draw Ellipse"},
        {"icon": "draw-arrow", "tooltip": "Draw Arrow"},
        {"icon": "draw-double-arrow", "tooltip": "Draw Double Arrow"},
        {"icon": "draw-line", "tooltip": "Draw Tooltip"},
        {"icon": "draw-coordinate-system", "tooltip": "Draw Coordinate System"},
        {"icon": "draw-spline", "tooltip": "Draw Spline"},
        {"icon": "shape-recognizer", "tooltip": "Draw Shape Recognizer"},
        {"icon": "snapping-grid", "tooltip": "Grid Snapping"},
        {"icon": "snapping-rotation", "tooltip": "Rotation Snapping"},
    ]

    selection_insertion_list = [
        {"icon": "select-rect", "tooltip": "Select Rectangle"},
        {"icon": "select-lasso", "tooltip": "Select Region"},
        {"icon": "object-select", "tooltip": "Select Object"},
        {"icon": "spacer", "tooltip": "Insert Vertical Space"},
        {"icon": "tool-image", "tooltip": "Insert Image"},
        {"icon": "edit-copy", "tooltip": "Copy Selection"},
        {"icon": "edit-cut", "tooltip": "Cut Selection"},
        {"icon": "edit-paste", "tooltip": "Paste Selection"},
    ]

    page_tool_list = [
        {"icon": "go-first-symbolic", "tooltip": "First Page"},
        {"icon": "go-previous-symbolic", "tooltip": "Previous Page"},
        {"icon": "xopp-page-annotated-next", "tooltip": "Next Annotated Page"},
        {"icon": "go-next-symbolic", "tooltip": "Next Page"},
        {"icon": "go-last-symbolic", "tooltip": "Last Page"},
        {"icon": "xopp-page-add", "tooltip": "Add Page"},
        {"icon": "xopp-page-delete", "tooltip": "Delete Page"},
    ]

    background_tool_list = [
        {"icon": "select-pdf-text-ht", "tooltip": "Select PDF Text Linear"},
        {"icon": "select-pdf-text-area", "tooltip": "Select PDF Text Area"},
        {"icon": "hand", "tooltip": "Hand Tool"},
        {"icon": "append-pdf-pages", "tooltip": "Append New PDF Pages"},
    ]

    audio_recording_list = [
        {"icon": "audio-record", "tooltip": "Record Audio"},
        {"icon": "audio-seek-backwards", "tooltip": "Seek Backwards"},
        {"icon": "audio-playback-pause", "tooltip": "Pause Playback"},
        {"icon": "audio-seek-forwards", "tooltip": "Seek Forwards"},
        {"icon": "audio-playback-stop", "tooltip": "Stop Playback"},
    ]
