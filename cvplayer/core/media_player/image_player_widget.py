from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from cvplayer.core.media_player.image_player_core.interface import *
from cvplayer.core.media_player.image_player_core.back_end.image_player import ImagePlayer 
from cvplayer.core.utils.widgets_utils import start_widget_basics
import cv2

class ImagePlayerWidget(QWidget):
    def __init__(self, custom_class) -> None:
        super().__init__()
        start_widget_basics(self, None, 'cvplayer/stylesheets/image_player_widget.css', minimum_height=300, minimum_width=300)
        self.custom_class = custom_class
        self.image_viewer = ImageViewer()
        self.image_player = ImagePlayer(self.image_viewer, self.custom_class.custom_method)
        self.build_ui_elements()

    def build_ui_elements(self):
        self.main_layout = QVBoxLayout(self)        
        self.top_layout = QHBoxLayout()
        
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addWidget(self.image_viewer)
        
        self.images_list = ImagesList(self.image_player,  self.top_layout)
        self.previous_image_button = PreviousImageButton(self.images_list,self.top_layout)
        self.image_counter = ImageCounter(self.images_list,self.top_layout)
        self.next_image_button = NextImageButton(self.images_list,self.top_layout)
        self.add_videos_button = AddImagesButton(self.images_list, self.top_layout)
        
        
    


from cvplayer import VideoPlayer
from ultralytics import YOLO
import cv2
from PyQt6.QtWidgets import QApplication
import sys

#yolov8 example
class CustomBase(): 
    def __init__(self) -> None:
        self.model = YOLO("/media/eduardo/HD 2tb/Downloads/yolov8s.pt")  # load a pretrained model 
    
    def custom_method(self, numpy_image): #method to be called on each frame and do whatever you want
        results = self.model(numpy_image)  # predict on an image
        for result in results:
            boxes = result.boxes  # Boxes object for bbox outputs
            classes = result.probs
            names = result.names
            print(boxes.cls)
            for box in boxes:
                cv2.rectangle(numpy_image, (int(box.xyxy[0][0]), int(box.xyxy[0][1])), (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (0, 255, 0), 2)
                cv2.putText(numpy_image, names[int(box.cls)], (int(box.xyxy[0][0]), int(box.xyxy[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
        
        return numpy_image #return the image with the changes
    
app = QApplication([])

x = ImagePlayerWidget(CustomBase()) #pass the class to the VideoPlayer and start the player
x.show()
sys.exit(app.exec())


