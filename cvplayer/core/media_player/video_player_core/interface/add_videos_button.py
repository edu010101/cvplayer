from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtGui import QPixmap, QIcon
from cvplayer.core.utils.widgets_utils import start_widget_basics
from pkg_resources import resource_filename

class AddVideosButton(QPushButton):
    def __init__(self, videos_list, layout=None):
        super().__init__()
        start_widget_basics(self, layout)
        self.set_css()
        self.videos_list = videos_list
        self.clicked.connect(self.get_videos)

    def get_videos(self):
        mp4_files = QFileDialog.getOpenFileNames(self, "Select videos", "", "Video Files (*.mp4 *.MP4 *.avi *.mov)")[0]
        if len(mp4_files) > 0:
            self.videos_list.add_videos(mp4_files)

    def set_css(self):
        add_icon_path = resource_filename(__name__, 'icons/add.png').replace('\\', '/')
        hover_icon_path = resource_filename(__name__, 'icons/add_hover.png').replace('\\', '/')
        pressed_icon_path = resource_filename(__name__, 'icons/add_pressed.png').replace('\\', '/')
        css_str = f"""
        QPushButton {{
            background-color: transparent;
            border-radius: 10px;
            border-image: url({add_icon_path});
            max-width: 50px;
            max-height: 50px;
            min-width: 50px;
            min-height: 50px;
            margin: 0%;
            padding: 0%;
            border: 0px;
        }}
        QPushButton:hover {{
            border-image: url({hover_icon_path});    
        }}
        QPushButton:pressed {{
            border-image: url({pressed_icon_path});
        }}
        """ 
        self.setStyleSheet(css_str)

        


        