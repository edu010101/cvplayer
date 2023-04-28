import cv2
class ImagePlayer():
    def __init__(self, image_viewer, custom_method) -> None:
        #it eill start the viewer, and then loads an default image on it
        #after that you will be able to change the image 
        self.image_viewer = image_viewer
        self.custom_method = custom_method
        self.image = None

    def set_image(self, image_path):
        self.image = cv2.imread(image_path)
        #self.custom_method(self.image)
        self.image_viewer.show_cv2_image(self.image)
        
    

    #the viewer have the defauklt image, and the image player will change it

        