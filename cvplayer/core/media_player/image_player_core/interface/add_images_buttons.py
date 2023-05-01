from PyQt6.QtWidgets import QPushButton, QFileDialog
from cvplayer.core.utils.widgets_utils import start_widget_basics


class AddImagesButton(QPushButton):
    def __init__(self, images_list, layout=None, CSS='cvplayer/stylesheets/add_videos_button.css'):
        super().__init__()
        start_widget_basics(self, layout, CSS)
        self.images_list = images_list
        self.clicked.connect(self.get_images)

    def get_images(self):
        images_files = QFileDialog.getOpenFileNames(self, "Select Images", "", "Image Files (*.jpg *.png *.jpeg *.JPG  *.PNG *.JPEG *.tif *.tiff *.npy)")[0]
        if len(images_files) > 0:
            self.images_list.add_images(images_files)



        


        