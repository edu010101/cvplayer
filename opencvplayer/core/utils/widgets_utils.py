from opencvplayer.core.utils import layout_utils, stylesheet_utils
from PyQt6.QtWidgets import QWidget, QLayout


def start_widget_basics(widget: QWidget, layout: QLayout = None, css_path: str = None, tool_tip: str = None, minimum_width: int=None, minimum_height: int=None, fixed_width: int=None, fixed_height: int=None) -> None:
    """Initialize widget CSS, Layout, ToolTip and Minimum Sizes"""
    if css_path!=None:
        stylesheet_utils.set_style_sheet(widget, css_path)
    if layout!=None:
        layout_utils.add_widget_in_layout(widget, layout)
    if tool_tip!=None:
        widget.setToolTip(tool_tip)
    if minimum_width!=None:
        widget.setMinimumWidth(minimum_width)
    if minimum_height!=None:
        widget.setMinimumHeight(minimum_height)
    if fixed_width!=None:
        widget.setFixedWidth(fixed_width)
    if fixed_height!=None:
        widget.setFixedHeight(fixed_height)
    
