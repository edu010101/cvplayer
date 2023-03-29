from PyQt6.QtWidgets import QApplication, QMainWindow
from opencvplayer.core.media_player.video_player_widget import VideoPlayerWidget
import sys

class VideoPlayer():
    def __init__(self, custom_class) -> None:
        #execute the app

        app = QApplication(sys.argv)
        video_player = VideoPlayerWidget(custom_class)
        window = QMainWindow()
        window.setCentralWidget(video_player)
        window.show()
        sys.exit(app.exec())


        
    

