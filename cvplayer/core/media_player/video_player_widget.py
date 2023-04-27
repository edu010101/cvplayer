from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from cvplayer.core.media_player.video_player_core.interface import *
from cvplayer.core.media_objects.video import Video
from cvplayer.core.media_player.video_player_core.back_end.video_player import VideoPlayer
from cvplayer.core.utils.widgets_utils import start_widget_basics


class VideoPlayerWidget(QWidget):
    def __init__(self, custom_class) -> None:
        super().__init__()
        start_widget_basics(self, None, 'cvplayer/stylesheets/video_player_widget.css', minimum_height=300, minimum_width=300)
        self.video = Video('cvplayer/core/utils/default.mp4')
        self.custom_class = custom_class
        self.video_player = VideoPlayer(self.video, self.custom_class)
        self.build_ui_elements()
        self.video_player.change_frame(0)

    def build_ui_elements(self):
        self.main_layout = QVBoxLayout(self)
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()
        
        self.main_layout.addLayout(self.top_layout)
        self.videos_list = VideosList(self.video_player,  self.top_layout)
        spacer = QSpacerItem(1, 10, hPolicy= QSizePolicy.Policy.Expanding)
        self.top_layout.addItem(spacer)
        self.add_videos_button = AddVideosButton(self.videos_list, self.top_layout)
        
        self.image_viewer = ImageViewer(self.main_layout)
        self.main_layout.addLayout(self.bottom_layout)
        
        self.previous_frame_button = PreviousFrameButton(self.video_player,self.bottom_layout)
        self.play_pause_button = PlayPauseButton(self.video_player,self.bottom_layout)
        self.next_frame_button = NextFrameButton(self.video_player,self.bottom_layout)
        self.video_slider = VideoSlider(self.video_player,self.bottom_layout)
        self.time_counter = TimeCounter(self.video_player,self.bottom_layout)
        self.video_speed_button = VideoSpeedButton(self.video_player,self.bottom_layout)

        self.video_player.add_ui_elements(self.image_viewer, self.time_counter, self.video_slider, self.play_pause_button)





