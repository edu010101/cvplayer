from PyQt6.QtWidgets import QApplication, QMainWindow
from cvplayer.core.media_player.video_player_widget import VideoPlayerWidget
import sys

class VideoPlayer():
    def __init__(self, custom_class) -> None:
        app = QApplication(sys.argv)
        if not hasattr(custom_class, 'custom_method') or not callable(getattr(custom_class, 'custom_method')):
            raise RuntimeError('custom_method not found in the class')
        video_player = VideoPlayerWidget(custom_class)
        window = QMainWindow()
        window.setStyleSheet('background-color: rgba(31,29,30,255);')
        window.setCentralWidget(video_player)
        window.setMinimumSize(550,400)
        window.show()
        sys.exit(app.exec())




    

