from PyQt6.QtWidgets import QLabel
from opencvplayer.core.utils.time_and_date_utils import milliseconds_to_counter_time

class TimeCounter(QLabel):
    def __init__(self, video_player, layout):
        super().__init__()
        self.video_player = video_player
        self.setText("00:00:00")
        self.setScaledContents(True)
        layout.addWidget(self)
        self.setStyleSheet("font-size: 20px; color: white;")

    def update_time(self, time_in_miliseconds):
        self.setText(milliseconds_to_counter_time(time_in_miliseconds))