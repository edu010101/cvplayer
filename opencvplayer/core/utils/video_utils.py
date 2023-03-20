from PyQt6.QtGui import QPixmap, QImage
import cv2

def calculate_time_beetwen_frames(video_fps):
    return 1 / video_fps

#temporariamente aqui
def cv2_image_to_QPixmap(cv2_image):
    height, width, channel = cv2_image.shape
    bytes_per_line = 3 * width
    qt_image = QImage(cv2_image.data, width, height, bytes_per_line, QImage.Format.Format_BGR888)
    
    return QPixmap(qt_image)

def get_video_thumbnail(road_video_path: str):
    video = cv2.VideoCapture(road_video_path)
    success, cv2_thumbnail = video.read()
    if success:
        return cv2_image_to_QPixmap(cv2_thumbnail)
    else:
        print("Error: Could not get thumbnail from video")
    video.release()
    cv2.destroyAllWindows()