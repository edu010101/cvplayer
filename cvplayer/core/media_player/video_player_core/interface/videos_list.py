from PyQt6.QtWidgets import QComboBox
from cvplayer.core.utils.widgets_utils import start_widget_basics
from cvplayer.core.media_objects.video import Video
import os

class VideosList(QComboBox):
    videos_dict = {}
    current_video_path = None
    video_player = None
    started = False
    def __init__(self, video_player, layout, css_path='cvplayer/stylesheets/videos_list.css',X=350,Y=40) -> None:
        super().__init__()
        start_widget_basics(self, layout, css_path, fixed_height=Y)
        self.video_player = video_player
        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.setMinimumWidth(X)
        self.currentIndexChanged.connect(self.change_video)
    
    def change_video(self, video_index):
        self.current_video_path = self.videos_dict[self.currentText()]
        self.video_player.set_video(Video(self.current_video_path))
        self.video_player.started.emit()

    def add_videos(self, videos_path):
        for video_path in videos_path:
            self.check_video_path(video_path)
            video_name = os.path.basename(video_path)
            self.videos_dict[video_name] = video_path
            self.addItem(video_name)
        
    def check_video_path(self, video_path):
        if not os.path.exists(video_path):
            raise FileNotFoundError("Video path not found")
        elif os.path.isfile(video_path):
            self.videos_list = [video_path]
