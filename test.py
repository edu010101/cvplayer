from opencvplayer import VideoPlayer
from mmdet.apis import inference_detector, init_detector


class CustomBase():
    def __init__(self) -> None:
        DetectionModelConfig='/home/edu0101/Desktop/labelme/labelme/modelo/FasterWithClasses/faster_rcnn_r50_fpn_1x_placas.py'
        DetectionModelWeights='/home/edu0101/Desktop/labelme/labelme/modelo/FasterWithClasses/epoch_50.pth'
        self.SignDetectionModel = init_detector(DetectionModelConfig, DetectionModelWeights, device='cpu')
        
    def custom_method(self, numpy_image):
        detection_result = inference_detector(self.SignDetectionModel, numpy_image)
        print(detection_result)
        return self.SignDetectionModel.show_result(
            numpy_image, detection_result, score_thr=0.7, show=False
        )
        


VideoPlayer(CustomBase())

