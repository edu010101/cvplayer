from PyQt6.QtWidgets import QPushButton
import cvplayer.core.utils.widgets_utils as widgets_utils
from PyQt6.QtGui import QKeySequence

class NextImageButton(QPushButton):
    def __init__(self, images_list, layout, CSS ='cvplayer/stylesheets/next_image_button.css', X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Right'))
        widgets_utils.start_widget_basics(self, layout, CSS, fixed_width=X,fixed_height=Y)
        self.images_list =  images_list
        self.pressed.connect(self.next_image)
    
    def next_image(self):
        if self.images_list.currentIndex() + 1 < self.images_list.count():
            self.images_list.setCurrentIndex(self.images_list.currentIndex() + 1)

class PreviousImageButton(QPushButton):
    def __init__(self, images_list, layout, CSS = 'cvplayer/stylesheets/previous_image_button.css', X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Right'))
        widgets_utils.start_widget_basics(self, layout, CSS, fixed_width=X,fixed_height=Y)
        self.images_list =  images_list
        self.pressed.connect(self.previous_image)
    
    def previous_image(self):
        if self.images_list.currentIndex() >= 1:
            self.images_list.setCurrentIndex(self.images_list.currentIndex() - 1)
