from PyQt6.QtWidgets import QPushButton
from PIL import ImageQt
import opencvplayer.core.utils.widgets_utils as widgets_utils

class PrintScreenButton(QPushButton):
    def __init__(self, widget_to_print, video_player, layout, CSS='opencvplayer/stylesheets/print_screen_button.css', tool_tip='Captura de tela', X=30, Y=30) -> None:
        super().__init__()
        widgets_utils.start_widget_basics(self, layout, CSS, tool_tip, fixed_width=X, fixed_height=Y)
        self.video_player = video_player
        self.clicked.connect(self.print_screen)
        self.widget_to_print = widget_to_print

    def print_screen(self):
        QPixmap_frame = self.widget_to_print.grab()
        print_image = ImageQt.fromqpixmap(QPixmap_frame)
        print_image.save("")

