from PyQt6.QtWidgets import QVBoxLayout
from PyQt6 import QtCore

def add_widget_in_layout(widget,layout, alignment= QtCore.Qt.AlignmentFlag.AlignVCenter):
    layout.addWidget(widget)#, alignment= alignment)

def add_layout_in_layout(layout_father, layout_son):
    layout_father.addLayout(layout_son)   

def add_spacer_in_layout(layout, spacer):
    layout.addSpacerItem(spacer)
    QVBoxLayout.addWidget