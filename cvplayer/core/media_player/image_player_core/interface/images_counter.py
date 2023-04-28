from PyQt6.QtWidgets import QLabel
from cvplayer.core.utils.widgets_utils import start_widget_basics

class ImageCounter(QLabel):
    def __init__(self, images_list, layout, CSS = 'cvplayer/stylesheets/image_counter.css', X=40, Y=40):
        super().__init__()
        self.images_list = images_list        
        start_widget_basics(self, layout, CSS, fixed_width=X,fixed_height=Y)
        self.set_image_counter()
        self.images_list.currentIndexChanged.connect(self.set_image_counter)
        self.images_list.image_added.connect(self.set_image_counter)

    def set_image_counter(self):
        self.setText(f'{self.images_list.currentIndex() + 1}/{self.images_list.count()}')