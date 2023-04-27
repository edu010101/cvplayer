import cv2

class Image():
    def __init__(self, image_path:str) -> None:
        self.image = cv2.imread(image_path)

    def get_image(self):
        return self.image
