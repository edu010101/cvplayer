import cv2
from opencvplayer.core.utils.video_utils import calculate_time_beetwen_frames

MINIMAL_FLOAT = 0.0000001

class Video:
    current_frame = None
    current_frame_id = 0
    current_milliseconds = 0
    current_seconds = 0
    
    def __init__(self, video_path: str, frames_to_jump: int = 1) -> None:
        self.video = cv2.VideoCapture(video_path)
        self.frames_to_jump = frames_to_jump
        self.fps = self.get_video_fps()
        self.total_number_of_frames = self.get_total_number_of_frames()

    def set_current_frame_id(self, frame_id: int) -> None:
        self.current_frame_id = frame_id

    def set_current_frame_position_by_index(self) -> None:
        self.video.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame_id)

    def set_frames_to_jump(self, frames_to_jump: int) -> None:
        self.frames_to_jump = frames_to_jump

    def grab_encoded_next_frame(self) -> None:
        self.video.grab()
    
    def decode_current_frame(self) -> None:
        _, self.current_frame = self.video.retrieve()

    def update_to_next_frame(self) -> None:
        _, self.current_frame = self.video.read()

    def update_current_frame_id(self) -> None:
        self.current_frame_id = self.get_current_frame_id()

    def update_video_time(self) -> None:
        self.current_milliseconds = self.get_milliseconds()
        self.current_seconds = self.get_seconds()
        
    def update_to_next_frame_based_on_frames_to_jump(self) -> None:
        for _ in range(self.frames_to_jump):
            self.grab_encoded_next_frame()
        
        self.decode_current_frame()
        
    #Basic a union of the last 3 methods
    def update_to_next_video_moment(self) -> None:
        """Iterates to the next frame and updates the video parameters"""
        self.update_to_next_frame_based_on_frames_to_jump()
        self.update_current_frame_id()
        self.update_video_time()
       
    def update_to_specific_video_moment(self) -> None:
        """Iterates to a specifc frame and updates the video parameters"""
        self.set_current_frame_position_by_index()
        self.decode_current_frame()
        self.update_current_frame_id()
        self.update_video_time()

    def get_milliseconds(self) -> int:
        return (self.current_frame_id / self.fps) * 1000
    
    def get_seconds(self) -> float:
        return self.current_frame_id / self.fps

    def get_current_frame_id(self) -> int:
        return int(self.video.get(cv2.CAP_PROP_POS_FRAMES))

    def get_total_number_of_frames(self) -> int:
        return self.video.get(cv2.CAP_PROP_FRAME_COUNT)

    def get_video_fps(self) -> float:
        return self.video.get(cv2.CAP_PROP_FPS)

    def get_time_between_frames(self) -> float:
        return calculate_time_beetwen_frames(self.fps)

    def close_video(self) -> None:
        self.video.release()