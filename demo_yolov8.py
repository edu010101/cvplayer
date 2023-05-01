from cvplayer import VideoPlayer
from ultralytics import YOLO
import cv2

# yolov8 example
class CustomBase(): 
    def __init__(self) -> None: #always load the model in the constructor
        self.model = YOLO("yolov8s.pt")  # load a pretrained model 
    
    def custom_method(self, numpy_image): #method to be called on each frame and do whatever you want(ALLWAYS RECIEVES THE IMAGE AS A NUMPY ARRAY)
        results = self.model(numpy_image)  # predict on an image
        for result in results:
            boxes = result.boxes  # Boxes object for bbox outputs
            classes = result.names
            for box in boxes: #just draw the boxes with the class name
                cv2.rectangle(numpy_image, (int(box.xyxy[0][0]), int(box.xyxy[0][1])), (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (0, 255, 0), 2)
                cv2.putText(numpy_image, classes[int(box.cls)], (int(box.xyxy[0][0]), int(box.xyxy[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
        return numpy_image #return the image with the changes (ALLWAYS RETURN THE IMAGE AS A NUMPY ARRAY WITH 3 CHANNELS)
    
VideoPlayer(CustomBase()) #pass the class to the VideoPlayer and start the player
















