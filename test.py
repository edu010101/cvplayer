from opencvplayer import VideoPlayer

from ultralytics import YOLO
import cv2

#yolov8 example
class CustomBase(): 
    def __init__(self) -> None:
        self.model = YOLO("/media/eduardo/HD 2tb/Downloads/yolov8s.pt")  # load a pretrained model 
    
    def custom_method(self, numpy_image): #method to be called on each frame and do whatever you want
        results = self.model(numpy_image)  # predict on an image
        for result in results:
            boxes = result.boxes  # Boxes object for bbox outputs
            for box in boxes:
                print(box.xyxy[0][1])
                cv2.rectangle(numpy_image, (int(box.xyxy[0][0]), int(box.xyxy[0][1])), (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (0, 255, 0), 2)
        
        return numpy_image #return the image with the changes
    
VideoPlayer(CustomBase()) #pass the class to the VideoPlayer and start the player



# from mmdet.apis import inference_detector, init_detector

# #mmdectection example
# class CustomBase():
#     def __init__(self) -> None:
#         DetectionModelConfig='/home/eduardo/labelme/labelme/modelo/FasterWithClasses/faster_rcnn_r50_fpn_1x_placas.py'
#         DetectionModelWeights='/home/eduardo/labelme/labelme/modelo/FasterWithClasses/epoch_50.pth'
#         self.SignDetectionModel = init_detector(DetectionModelConfig, DetectionModelWeights, device='cuda:0')
        
#     def custom_method(self, numpy_image):
#         detection_result = inference_detector(self.SignDetectionModel, numpy_image)
#         print(detection_result)
#         return self.SignDetectionModel.show_result(
#             numpy_image, detection_result, score_thr=0.7, show=False
#         )
    






















