from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QMainWindow
from opencvplayer.core.media_player.video_player_core.interface import *
from opencvplayer.core.media_objects.video import Video
from opencvplayer.core.media_player.video_player_core.back_end.video_player import VideoPlayer
#from media_player.video_player_core.back_end.videos_manager import VideosManager
from opencvplayer.core.utils.widgets_utils import start_widget_basics

from mmdet.apis import inference_detector, init_detector


class VideoPlayerWidget(QWidget):
    
    def __init__(self, videos_path: str= '/media/eduardo/HD 2tb/Downloads/HD Simulado') -> None:
        super().__init__()
        start_widget_basics(self, None, 'opencvplayer/stylesheets/video_player_widget.css', minimum_height=300, minimum_width=300)
        self.video = Video('opencvplayer/core/utils/default.mp4')
        self.videos_path = videos_path
        self.custom_class = CustomBase()
        self.video_player = VideoPlayer(self.video, self.custom_class)
        self.build_ui_elements()
        #self.video_player.change_frame(0)

    def build_ui_elements(self):
        self.vertical_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout()
        
        self.videos_list = VideosList(self, ['/media/eduardo/HD 2tb/Downloads/HD Simulado/MS-112/MS-112_C_01_R0/MS-112_C_02_R0.mp4', '/media/eduardo/HD 2tb/Downloads/HD Simulado/MS-112/MS-112_C_01_R0/MS-112_C_01_R0.mp4'], self.vertical_layout)
        self.image_viewer = ImageViewer(self.vertical_layout)
        self.vertical_layout.addLayout(self.horizontal_layout)
        
        self.previous_frame_button = PreviousFrameButton(self.video_player,self.horizontal_layout)
        self.play_pause_button = PlayPauseButton(self.video_player,self.horizontal_layout)
        self.next_frame_button = NextFrameButton(self.video_player,self.horizontal_layout)
        self.video_slider = VideoSlider(self.video_player,self.horizontal_layout)
        self.time_counter = TimeCounter(self.video_player,self.horizontal_layout)
        self.video_speed_button = VideoSpeedButton(self.video_player,self.horizontal_layout)

        self.video_player.add_ui_elements(self.image_viewer, self.time_counter, self.video_slider, self.play_pause_button)
    
    def change_video(self, video_path):
        self.video = Video(video_path)
        self.video_player = VideoPlayer(self.video, self.custom_class)
        self.build_ui_elements()
        self.video_player.change_frame(0)


class CustomBase():
    def __init__(self) -> None:
        DetectionModelConfig='/home/eduardo/labelme/labelme/modelo/SignDetectorConfig.py'
        DetectionModelWeights='/home/eduardo/labelme/labelme/modelo/SignDetectorWeights.pth'
        self.SignDetectionModel = init_detector(DetectionModelConfig, DetectionModelWeights, device='cuda:0')

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
window.setCentralWidget(VideoPlayerWidget())
window.show()