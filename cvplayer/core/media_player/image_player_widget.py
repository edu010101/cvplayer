from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from cvplayer.core.media_player.image_player_core.interface import *
from cvplayer.core.media_player.image_player_core.back_end.image_player import ImagePlayer 
from cvplayer.core.utils.widgets_utils import start_widget_basics
import cv2

class ImagePlayerWidget(QWidget):
    def __init__(self, custom_class) -> None:
        super().__init__()
        start_widget_basics(self, None, 'stylesheets/image_player_widget.css', minimum_height=300, minimum_width=300)
        self.custom_class = custom_class
        self.image_viewer = ImageViewer()
        self.image_player = ImagePlayer(self.image_viewer, self.custom_class.custom_method)
        self.build_ui_elements()

    def build_ui_elements(self):
        self.main_layout = QVBoxLayout(self)        
        self.top_layout = QHBoxLayout()
        
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addWidget(self.image_viewer)#, alignment= Qt.AlignmentFlag.AlignCenter)
        
        self.images_list = ImagesList(self.image_player,  self.top_layout)
        self.top_layout.addSpacerItem(QSpacerItem(0,0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.previous_image_button = PreviousImageButton(self.images_list,self.top_layout)
        self.image_counter = ImageCounter(self.images_list,self.top_layout)
        self.next_image_button = NextImageButton(self.images_list,self.top_layout)
        self.top_layout.addSpacerItem(QSpacerItem(0,0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.add_videos_button = AddImagesButton(self.images_list, self.top_layout)
        
        