from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import pyqtSignal, Qt
from cvplayer.core.utils.widgets_utils import start_widget_basics
import os
from pkg_resources import resource_filename

class ImagesList(QComboBox):
    images_dict = {}
    image_added = pyqtSignal()
    current_image_path = None
    image_player = None

    def __init__(self, image_player, layout,X=350,Y=40) -> None:
        super().__init__()
        start_widget_basics(self, layout, fixed_height=Y)
        self.set_css()
        self.image_player = image_player
        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.setMinimumWidth(X)
        self.currentIndexChanged.connect(self.set_current_image)

    def set_current_image(self, image_index):
        self.current_image_path = self.images_dict[self.currentText()]
        self.image_player.set_image(self.current_image_path)

    def add_images(self, images_path):
        for image_path in images_path:
            self.check_video_path(image_path)
            image_name = os.path.basename(image_path)
            self.images_dict[image_name] = image_path
            self.addItem(image_name)
        self.image_added.emit()
        #self.setCurrentIndex(-1)
        
    def check_video_path(self, video_path):
        if not os.path.exists(video_path):
            raise FileNotFoundError("Image path not found")
        elif os.path.isfile(video_path):
            return True

    def set_css(self):
        css_str = """
        QComboBox {
            border-radius: 7px;
            color: lightgray;
            background-color: #333333;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            min-width: 350px;
            max-width: 350px;
        }
        QComboBox::hover{

            background-color:  #4e5050;
            border-radius: 5px;
        }
        QComboBox:!editable:on, QComboBox::drop-down:editable:on {
            background: #4e5050;
        }
        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;
            border-bottom-right-radius: 3px;
            border-radius: 5px;
        }
        QComboBox::down-arrow {
            image: url(""" + resource_filename(__name__, 'icons/drop_down.png').replace("\\", "/") + """);
            height: 15px;
            width: 15px;
        } 
        QComboBox QAbstractItemView {
            border-radius: 5px;
            selection-color: #4e5050;
            selection-background-color: #4e5050;
            color: rgba(91,91,91,255);
            background-color: #4e5050;
            outline: 0px;
            font-size: 12pt;
            font-weight: 400;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        QListView::item {
            height:40px;
            outline: 0px;
        }
        QListView::item:selected {
            background-color: #4e5050;
            outline: 0px;
        }
        QScrollBar{
            width:0px;
        }"""
        self.setStyleSheet(css_str)