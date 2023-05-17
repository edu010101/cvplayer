from PyQt6.QtWidgets import QPushButton
import cvplayer.core.utils.widgets_utils as widgets_utils
from PyQt6.QtGui import QKeySequence
from pkg_resources import resource_filename
class NextImageButton(QPushButton):
    def __init__(self, images_list, layout, X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Right'))
        widgets_utils.start_widget_basics(self, layout, fixed_width=X,fixed_height=Y)
        self.set_css()
        self.images_list =  images_list
        self.pressed.connect(self.next_image)
    
    def next_image(self):
        if self.images_list.currentIndex() + 1 < self.images_list.count():
            self.images_list.setCurrentIndex(self.images_list.currentIndex() + 1)
    
    def set_css(self):
        css_str = """
        QPushButton{
            border-image: url("""+ resource_filename(__name__, 'icons/next2.png') +""");
            background:transparent;       
            border-radius: 10px;
            border: none;
            outline: none;
        }
        QPushButton:hover {
            background-color: rgba(206, 197, 197, 0.21);
        }
        QPushButton:pressed{
            background-color: rgba(132, 129, 129, 0.264);
        }
        """
        self.setStyleSheet(css_str)

class PreviousImageButton(QPushButton):
    def __init__(self, images_list, layout, X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Left'))
        widgets_utils.start_widget_basics(self, layout, fixed_width=X,fixed_height=Y)
        self.set_css()
        self.images_list =  images_list
        self.pressed.connect(self.previous_image)
    
    def previous_image(self):
        if self.images_list.currentIndex() >= 1:
            self.images_list.setCurrentIndex(self.images_list.currentIndex() - 1)
    
    def set_css(self):
        css_str = """
        QPushButton{
            border-image: url("""+ resource_filename(__name__, 'icons/previous2.png') +""");
            background:transparent;       
            border-radius: 10px;
            border: none;
            outline: none;
        }
        QPushButton:hover {
            background-color: rgba(206, 197, 197, 0.21);
        }
        QPushButton:pressed{
            background-color: rgba(132, 129, 129, 0.264);
        }
        """
        self.setStyleSheet(css_str)


