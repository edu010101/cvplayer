from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSpinBox
from PyQt6.QtGui import QShortcut
import cvplayer.core.utils.widgets_utils as widgets_utils
from PyQt6.QtGui import QKeySequence

class VideoSpeedButton(QSpinBox):
    def __init__(self, video_player, layout, CSS='stylesheets/video_speed_button.css'):
        super().__init__()
        widgets_utils.start_widget_basics(self, layout, CSS, tool_tip='Change video speed by pressing up and down arrows')
        self.setSuffix(' x')
        self.valueChanged.connect(video_player.change_speed)
        self.setValue(1)
        self.setReadOnly(True)
        self.start_shortcuts()
        

    def increase_speed(self):
        self.setValue(self.value() + 1)
    
    def decrease_speed(self):
        if self.value() > 1:
            self.setValue(self.value() - 1)

    def start_shortcuts(self):
        self.increase_speed_shortcut = QShortcut(QKeySequence('Up'), self)
        self.increase_speed_shortcut.activated.connect(self.increase_speed)
        self.decrease_speed_shortcut = QShortcut(QKeySequence('Down'), self)
        self.decrease_speed_shortcut.activated.connect(self.decrease_speed)
    
    
    

            

     
