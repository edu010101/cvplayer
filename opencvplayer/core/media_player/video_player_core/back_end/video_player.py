from opencvplayer.core.updater.video_updater import VideoUpdater
from opencvplayer.core.media_objects.video import Video
import time



class VideoPlayer():
    def __init__(self, video: Video = None, custom_class=None, viewer = None, time_counter = None, slider = None, play = None) -> None:
        
        ###TALVEZ SAIA
        self.video = video
        self.viewer = viewer
        self.time_counter = time_counter
        self.slider = slider
        self.play = play
        self.start  = time.time()
        self.end = time.time()

        self.create_video_updater()
        self.current_time = time.time()

        self.custom_class = custom_class
        

#comand to install pytorch 1.13
#pip install torch==1.3.1 torchvision==0.4.2 -f https://download.pytorch.org/whl/torch_stable.html


        
    def play_video(self) -> None:
        self.video_updater.start_time_updater()

    def pause_video(self) -> None:
        self.video_updater.stop_time_updater()

    def change_frame(self, frame_id : int)-> None:
        if 0 <= frame_id < self.video.total_number_of_frames:
            self.video_updater.stop_time_updater()
            self.video.set_current_frame_id(frame_id)
            self.video_updater.start_signal_updater()

    def change_speed(self, speed: int):
        """speed is a positive integer, 1 is normal speed, 2 is double speed, 3 is triple speed, etc."""
        self.video.set_frames_to_jump(speed)
    
    def show_frame(self):
        self.viewer.show_cv2_image(self.video.current_frame)
    
    def add_ui_elements(self, viewer, time_counter, slider, play):
        self.viewer = viewer
        self.time_counter = time_counter
        self.slider = slider
        self.play = play
    
    def set_video(self, video: Video):
        self.video = video
    
    def update_ui_elements_each_second(self):
        if self.current_time + 1 < time.time():
            self.current_time = time.time()
            self.slider.set_value(self.video.current_frame_id)
            self.time_counter.update_time(self.video.current_milliseconds)

    def update_ui_elements(self):
        self.slider.set_value(self.video.current_frame_id)
        self.time_counter.update_time(self.video.current_milliseconds)
        self.play.set_play()
        
    def start_time(self):
        self.start = time.time()
    
    def end_time(self):
        self.end = time.time()
        print(self.end - self.start)

    def custom_method(self):
        self.video.current_frame =  self.custom_class.custom_method(self.video.current_frame)

    def create_video_updater(self):
        self.video_updater = VideoUpdater(self.video.fps)
        
        self.video_updater.add_method_on_timer_updater('update_frame', self.video.update_to_next_video_moment)
        self.video_updater.add_method_on_timer_updater('update_viewer', self.custom_method)
        self.video_updater.add_method_on_timer_updater('update_viewe', self.show_frame)
        self.video_updater.add_method_on_timer_updater('update_ui_elements', self.update_ui_elements_each_second)
        

        
        self.video_updater.add_method_on_signal_updater('jump_to_frame', self.video.update_to_specific_video_moment)
        self.video_updater.add_method_on_signal_updater('update_viewer', self.custom_method)
        self.video_updater.add_method_on_signal_updater('update_viewe', self.show_frame)
        self.video_updater.add_method_on_signal_updater('update_ui_elements', self.update_ui_elements)
        


