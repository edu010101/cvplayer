## Description

Welcome to **OpenCVPlayer**, a powerful and easy to use tool for visualizing computer vision models and their inferences. With OpenCVPlayer, you can easily view and analyze the output of your models, no mather wich library or framework you are using, saving you from long codes for a simple inference visualization.

## Features
- [x] Video inference visualization.
- [ ] Images inference visualization.
- [x] Frame level control.
- [x] Easy to use.
- [ ] Portable for PyQt6 aplications.

## Requirements

### pip

```bash
# inside your env
pip install PyQt6==6.4.2 PyQt6-Qt6==6.4.2 PyQt6-sip==13.4.1
pip install opencv-python
```
## Instalation

```bash
# inside your env
git clone https://github.com/edu010101/opencvplayer
cd opencvplayer
pip install -e .
```
## Usage

### Video Player

```python
from opencvplayer import VideoPlayer

#create a class with any name
class ExampleName():
    def __init___(self): #it can have many args as you need
        #initialize your model
    
    #your class NEED to have this method with this exactly name.
    def custom_method(self, numpy_image): #this method can have just the np.array parameter
      	#this method receives an np.array representing your image or frame
      	#then modify and inference your array as you want
	
    	return numpy_image  #then return your modified np.array

VideoPlayer(ExampleName()) #load your class as an argument to the player
```
### Image Player

```python
from opencvplayer import ImagePlayer

#create a class with any name
class ExampleClass():
    def __init___(self): #it can have many args as you need
        #initialize your model
    
    #your class NEED to have this method with this exactly name.
    def custom_method(self, numpy_image):
      	#this method receives an np.array representing your image or frame
      	#modify and inference your array as you want
	
    	return numpy_image  #then return your modified np.array

imageclassifier = ExampleClass()
ImagePlayer(imageclassifier) #load your class as an argument to the player
```

### Yolov8 demo

```python
from opencvplayer import VideoPlayer
from ultralytics import YOLO
import cv2

#yolov8 example
class CustomBase(): 
    def __init__(self) -> None:
        self.model = YOLO("/path_to_weights/yolov8s.pt")  # load a pretrained model 
    
    def custom_method(self, numpy_image): #method to be called on each frame and do whatever you want
        results = self.model(numpy_image)  # predict on an image
        for result in results:
            boxes = result.boxes  # Boxes object for bbox outputs
            for box in boxes:
                print(box.xyxy[0][1])
                cv2.rectangle(numpy_image, (int(box.xyxy[0][0]), int(box.xyxy[0][1])), (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (0, 255, 0), 2)
        
        return numpy_image #return the image with the changes
    
VideoPlayer(CustomBase()) #pass the class to the VideoPlayer and start the player
```

### mmdetection demo

```python
from opencvplayer import VideoPlayer
from mmdet.apis import inference_detector, init_detector

#mmdectection example
class FasterRCNN():
    def __init__(self) -> None:
        DetectionModelConfig='/path_to_config/faster_rcnn_r50_fpn_1x_placas.py'
        DetectionModelWeights='/path_to_weights/epoch_50.pth'
        self.SignDetectionModel = init_detector(DetectionModelConfig, DetectionModelWeights, device='cuda:0')
        
    def custom_method(self, numpy_image):
        detection_result = inference_detector(self.SignDetectionModel, numpy_image)
        print(detection_result)
        return self.SignDetectionModel.show_result(
            numpy_image, detection_result, score_thr=0.7, show=False
        )

VideoPlayer(FasterRCNN())
```