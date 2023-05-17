from PyQt6.QtWidgets import QPushButton, QFileDialog
from cvplayer.core.utils.widgets_utils import start_widget_basics
from pkg_resources import resource_filename

class AddImagesButton(QPushButton):
    def __init__(self, images_list, layout=None):
        super().__init__()
        start_widget_basics(self, layout)
        self.set_css()
        self.images_list = images_list
        self.clicked.connect(self.get_images)

    def get_images(self):
        images_files = QFileDialog.getOpenFileNames(self, "Select Images", "", "Image Files (*.jpg *.png *.jpeg *.JPG  *.PNG *.JPEG *.tif *.tiff *.npy)")[0]
        if len(images_files) > 0:
            self.images_list.add_images(images_files)

    def set_css(self):
        add_icon_path = resource_filename(__name__, 'icons/add.png')
        hover_icon_path = resource_filename(__name__, 'icons/add_hover.png')
        pressed_icon_path = resource_filename(__name__, 'icons/add_pressed.png')
        css_str = f"""
        QPushButton {{
            background-color: transparent;
            border-radius: 10px;
            border-image: url({add_icon_path});
            max-width: 50px;
            max-height: 50px;
            min-width: 50px;
            min-height: 50px;
            margin: 0%;
            padding: 0%;
            border: 0px;
        }}
        QPushButton:hover {{
            border-image: url({hover_icon_path});    
        }}
        QPushButton:pressed {{
            border-image: url({pressed_icon_path});
        }}
        """ 
        self.setStyleSheet(css_str)



        


        