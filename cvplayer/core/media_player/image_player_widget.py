from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from cvplayer.core.media_player.image_player_core.interface import *
#from cvplayer.core.media_objects.image import Video
from cvplayer.core.media_player.image_player_core.back_end.image_player import ImagePlayer 
from cvplayer.core.utils.widgets_utils import start_widget_basics
import cv2

class ImagePlayerWidget(QWidget):
    def __init__(self, custom_class) -> None:
        super().__init__()
        start_widget_basics(self, None, 'cvplayer/stylesheets/image_player_widget.css', minimum_height=300, minimum_width=300)
        self.image = cv2.imread('cvplayer/icons/placeholder.png')
        self.custom_class = custom_class
        self.image_player = ImagePlayer(self.image, self.custom_class)
        self.build_ui_elements()

    def build_ui_elements(self):
        self.main_layout = QVBoxLayout(self)
        self.top_layout = QHBoxLayout()
        
        self.main_layout.addLayout(self.top_layout)
        self.images_list = ImagesList(self.image_player,  self.top_layout)
        spacer = QSpacerItem(1, 10, hPolicy= QSizePolicy.Policy.Expanding)
        self.top_layout.addItem(spacer)
        self.add_videos_button = AddImagesButton(self.images_list, self.top_layout)
        
        self.image_viewer = ImageViewer(self.main_layout)
    
        self.previous_image_button = PreviousImageButton(self.video_player,self.bottom_layout)
        self.next_image_button = NextImageButton(self.video_player,self.bottom_layout)
        
        self.image_counter = ImageCounter(self.video_player,self.bottom_layout)

        #self.video_player.add_ui_elements(self.image_viewer, self.time_counter, self.video_slider, self.play_pause_button)





