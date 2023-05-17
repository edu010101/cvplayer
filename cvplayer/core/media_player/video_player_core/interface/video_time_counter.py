from PyQt6.QtWidgets import QLabel
from cvplayer.core.utils.time_and_date_utils import milliseconds_to_counter_time
from cvplayer.core.utils.widgets_utils import start_widget_basics

class TimeCounter(QLabel):
    def __init__(self, video_player, layout, CSS='stylesheets/video_time_counter.css'):
        super().__init__()
        self.video_player = video_player
        start_widget_basics(self, layout, CSS)
        self.setText("00:00:00")
        self.setScaledContents(True)
        #self.setStyleSheet("background-color: rgb(200,200,200); font-size: 20px; color: black;")

        #layout.addWidget(self)

    def update_time(self, time_in_miliseconds):
        self.setText(milliseconds_to_counter_time(time_in_miliseconds))