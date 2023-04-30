from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import pyqtSignal, Qt
from cvplayer.core.utils.widgets_utils import start_widget_basics
import os

class ImagesList(QComboBox):
    images_dict = {}
    image_added = pyqtSignal()
    current_image_path = None
    image_player = None

    def __init__(self, image_player, layout, css_path='cvplayer/stylesheets/videos_list.css',X=350,Y=40) -> None:
        super().__init__()
        start_widget_basics(self, layout, css_path, fixed_height=Y)
        self.image_player = image_player
        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.setMinimumWidth(X)
        self.currentIndexChanged.connect(self.set_current_image)

    def set_current_image(self, image_index):
        self.current_image_path = self.images_dict[self.currentText()]
        self.image_player.set_image(self.current_image_path)

    def add_images(self, images_path):
        for image_path in images_path:
            self.check_video_path(image_path)
            image_name = os.path.basename(image_path)
            self.images_dict[image_name] = image_path
            self.addItem(image_name)
        self.image_added.emit()
        #self.setCurrentIndex(-1)
        
    def check_video_path(self, video_path):
        if not os.path.exists(video_path):
            raise FileNotFoundError("Image path not found")
        elif os.path.isfile(video_path):
            return True
