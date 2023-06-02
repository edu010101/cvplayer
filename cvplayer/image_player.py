from PyQt6.QtWidgets import QApplication, QMainWindow
from cvplayer.core.media_player.image_player_widget import ImagePlayerWidget
import sys

class ImagePlayer():
    def __init__(self, custom_class) -> None:
        app = QApplication(sys.argv)
        if not hasattr(custom_class, 'custom_method') or not callable(getattr(custom_class, 'custom_method')):
            raise RuntimeError('custom_method not found in the class')
        image_player = ImagePlayerWidget(custom_class)
        window = QMainWindow()
        window.setStyleSheet('background-color: rgba(31,29,30,255);')
        window.setMinimumSize(550,400)
        window.setCentralWidget(image_player)
        window.show()
        sys.exit(app.exec())

