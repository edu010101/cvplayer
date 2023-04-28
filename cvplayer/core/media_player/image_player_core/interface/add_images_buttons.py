from PyQt6.QtWidgets import QPushButton, QFileDialog
from cvplayer.core.utils.widgets_utils import start_widget_basics


class AddImagesButton(QPushButton):
    def __init__(self, videos_list, layout=None, CSS='cvplayer/stylesheets/add_videos_button.css'):
        super().__init__()
        start_widget_basics(self, layout, CSS)
        self.setText('Add Videos')
        self.videos_list = videos_list
        self.clicked.connect(self.get_images)

    def get_images(self):
        images_files = QFileDialog.getOpenFileNames(self, "Select videos", "", "Video Files (*.jpg *.png *.jpeg *.mp4)")[0]
        if len(images_files) > 0:
            self.videos_list.add_images(images_files)



        


        