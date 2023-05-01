import cv2
import os
import numpy as np
class ImagePlayer():
    def __init__(self, image_viewer, custom_method) -> None:
        #it eill start the viewer, and then loads an default image on it
        #after that you will be able to change the image 
        self.image_viewer = image_viewer
        self.custom_method = custom_method
        self.image = None

    def set_image(self, image_path):
        if os.path.splitext(image_path)[1] == '.npy':
            self.image = np.load(image_path)
        else:
            self.image = cv2.imread(image_path)
        self.image = self.check_image(self.image)
        self.image_viewer.show_cv2_image(self.custom_method(self.image))
        
    def check_image(self, image):
        w, h, c = image.shape
        if image is None or w == 0 or h == 0 or c == 0:
            raise ValueError("Image is not valid")
        if c > 3:
            image = image[:, :, :3]
            image = image.astype(np.uint8)
            print("Image has more than 3 channels, it will be converted to 3 channels")
        return image
        