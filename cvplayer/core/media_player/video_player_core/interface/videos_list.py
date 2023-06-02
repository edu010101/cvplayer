from PyQt6.QtWidgets import QComboBox
from cvplayer.core.utils.widgets_utils import start_widget_basics
from cvplayer.core.media_objects.video import Video
import os
from pkg_resources import resource_filename

class VideosList(QComboBox):
    videos_dict = {}
    current_video_path = None
    video_player = None
    started = False
    def __init__(self, video_player, layout,X=350,Y=40) -> None:
        super().__init__()
        start_widget_basics(self, layout, fixed_height=Y)
        self.set_css()
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

    def set_css(self):
        image_path = resource_filename(__name__, 'icons/drop_down.png').replace("\\", "/")
        css_str = """
        QComboBox {
            border-radius: 7px;
            color: lightgray;
            background-color: #333333;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            min-width: 350px;
            max-width: 350px;
        }
        QComboBox::hover{

            background-color:  #4e5050;
            border-radius: 5px;
        }
        QComboBox:!editable:on, QComboBox::drop-down:editable:on {
            background: #4e5050;
        }
        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;
            border-bottom-right-radius: 3px;
            border-radius: 5px;
        }
        QComboBox::down-arrow {
            image: url(""" + image_path + """);
            height: 15px;
            width: 15px;
        } 
        QComboBox QAbstractItemView {
            border-radius: 5px;
            selection-color: #4e5050;
            selection-background-color: #4e5050;
            color: rgba(91,91,91,255);
            background-color: #4e5050;
            outline: 0px;
            font-size: 12pt;
            font-weight: 400;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        QListView::item {
            height:40px;
            outline: 0px;
        }
        QListView::item:selected {
            background-color: #4e5050;
            outline: 0px;
        }
        QScrollBar{
            width:0px;
        }"""
        self.setStyleSheet(css_str)