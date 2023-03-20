from PyQt6.QtWidgets import QComboBox
from opencvplayer.core.utils.widgets_utils import start_widget_basics
import os

class VideosList(QComboBox):
    videos_dict = {}
    current_video = None
    video_player = None

    def __init__(self, video_player, videos_path, layout, css_path='opencvplayer/stylesheets/videos_list.css',X=30,Y=32) -> None:
        super().__init__()
        start_widget_basics(self, layout, css_path, fixed_height=Y)
        self.video_player = video_player
        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.videos_list = videos_path
        self.populate_video_dict(videos_path)
        self.currentIndexChanged.connect(self.change_video)

    def change_video(self, video_name):
        self.current_video = self.videos_dict[video_name]
        self.video_player.change_video(self.current_video)

    def populate_video_dict(self, videos_path):
        self.clear()
        

        for video_path in self.videos_list:
            self.check_video_path(video_path)
            video_name = os.path.basename(video_path)
            self.addItem(video_name)
            self.videos_dict[video_name] = video_path

    def check_video_path(self, video_path):
        if not os.path.exists(video_path):
            raise FileNotFoundError("Video path not found")
        elif os.path.isfile(video_path):
            self.videos_list = [video_path]
