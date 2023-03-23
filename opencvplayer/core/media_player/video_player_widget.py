from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QMainWindow, QSpacerItem, QSizePolicy
from opencvplayer.core.media_player.video_player_core.interface import *
from opencvplayer.core.media_objects.video import Video
from opencvplayer.core.media_player.video_player_core.back_end.video_player import VideoPlayer

from opencvplayer.core.utils.widgets_utils import start_widget_basics
from mmdet.apis import inference_detector, init_detector


class VideoPlayerWidget(QWidget):
    def __init__(self, custom_class) -> None:
        super().__init__()
        start_widget_basics(self, None, 'opencvplayer/stylesheets/video_player_widget.css', minimum_height=300, minimum_width=300)
        self.video = Video('opencvplayer/core/utils/default.mp4')
        self.custom_class = custom_class
        self.video_player = VideoPlayer(self.video, self.custom_class)
        self.build_ui_elements()

    def build_ui_elements(self):
        self.main_layout = QVBoxLayout(self)
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()
        
        self.main_layout.addLayout(self.top_layout)
        self.videos_list = VideosList(self.video_player,  self.top_layout)
        spacer = QSpacerItem(1, 10, hPolicy= QSizePolicy.Policy.Expanding)
        self.top_layout.addItem(spacer)
        self.add_videos_button = AddVideosButton(self.videos_list, self.top_layout)
        
        self.image_viewer = ImageViewer(self.main_layout)
        self.main_layout.addLayout(self.bottom_layout)
        
        self.previous_frame_button = PreviousFrameButton(self.video_player,self.bottom_layout)
        self.play_pause_button = PlayPauseButton(self.video_player,self.bottom_layout)
        self.next_frame_button = NextFrameButton(self.video_player,self.bottom_layout)
        self.video_slider = VideoSlider(self.video_player,self.bottom_layout)
        self.time_counter = TimeCounter(self.video_player,self.bottom_layout)
        self.video_speed_button = VideoSpeedButton(self.video_player,self.bottom_layout)

        self.video_player.add_ui_elements(self.image_viewer, self.time_counter, self.video_slider, self.play_pause_button)


class CustomBase():
    def __init__(self) -> None:
        #DetectionModelConfig='/home/eduardo/labelme/labelme/modelo/SignDetectorConfig.py'
        #DetectionModelWeights='/home/eduardo/labelme/labelme/modelo/SignDetectorWeights.pth'
        #self.SignDetectionModel = init_detector(DetectionModelConfig, DetectionModelWeights, device='cuda:0')
        pass
    def custom_method(self, numpy_image):
        # detection_result = inference_detector(self.SignDetectionModel, numpy_image)
        # print(detection_result)
        # return self.SignDetectionModel.show_result(
        #     numpy_image, detection_result, score_thr=0.3, show=False
        # )
        return numpy_image

from PyQt6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setStyleSheet("""QWidget{background-color: rgba(1,1,1,255);}""")
custm = CustomBase()
window.setCentralWidget(VideoPlayerWidget(custm))
window.show()