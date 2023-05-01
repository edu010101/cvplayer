from cvplayer import ImagePlayer
from mmdet.apis import inference_detector, init_detector

#mmdectection example
class CustomBase():
    def __init__(self) -> None: #always load the model in the constructor
        model_config='your_path_to_config/faster_rcnn_r50_fpn_1x.py' #you can use any model from mmdetection
        model_weights='your_path_to_weights/epoch_50.pth' 
        self.detection_model = init_detector(model_config, model_weights, device='cuda:0')
        
    def custom_method(self, numpy_image):
        detection_result = inference_detector(self.detection_model, numpy_image)
        return self.detection_model.show_result(numpy_image, detection_result, score_thr=0.7, show=False)

ImagePlayer(CustomBase()) #pass the class to the ImagePlayer and start the player







