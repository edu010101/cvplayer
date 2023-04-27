from PyQt6.QtWidgets import QComboBox
from utils import WidgetsUtils
import os

class VideosManager():
    def __init__(self, video_player_widget) -> None:
        self.video_player_widget = video_player_widget
        self.videos_dict = {}
        self.current_video = None
        
        self.populate_videos_dict(videos_path)

    def __init__(self, video_player, videos_path, layout, css_path='stylesheets/videos_list.css',X=30,Y=32) -> None:
        super().__init__()
        start_widget_basics(self, layout, css_path, fixed_height=Y)
        self.video_player = video_player
        self.setInsertPolicy(QComboBox.NoInsert)
        self.populate_video_dict(videos_path)

    def populate_videos_dict(self, videos_path):
        self.clear()
        self.check_video_path(videos_path)

        for video_path in self.videos_list:
            video_name = os.path.basename(video_path)
            self.addItem(video_name)
            self.videos_dict[video_name] = video_path

    def check_video_path(self, video_path):
        if not os.path.exists(video_path):
            raise FileNotFoundError("Video path not found")
        elif os.path.isdir(video_path):
            self.videos_list = self.find_all_mp4(video_path)
        elif os.path.isfile(video_path):
            self.videos_list = [video_path]

    def find_all_mp4(self, path):
        return glob.glob(os.path.join(path, '**', '*.mp4'), recursive=True)
