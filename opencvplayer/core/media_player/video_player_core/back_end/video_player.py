from opencvplayer.core.updater.video_updater import VideoUpdater
from opencvplayer.core.media_objects.video import Video
import time



class VideoPlayer():
    def __init__(self, video: Video = None, custom_class=None) -> None:
        self.video = video
        self.create_video_updater()
        self.current_time = time.time()
        self.custom_class = custom_class
                
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
        self.video_updater.stop_time_updater()
        self.video = video
        self.create_video_updater()  
        self.change_frame(0)
        self.slider.set_range(self.video.total_number_of_frames)
        self.update_ui_elements()
    
    def update_ui_elements_each_second(self):
        if self.current_time + 1 < time.time():
            self.current_time = time.time()
            self.slider.set_value(int(self.video.current_frame_id))
            self.time_counter.update_time(self.video.current_milliseconds)

    def update_ui_elements(self):
        self.slider.set_value(self.video.current_frame_id)
        self.time_counter.update_time(self.video.current_milliseconds)
        self.play.set_play()

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
        


