from PyQt6.QtWidgets import QPushButton, QToolButton
import cvplayer.core.utils.widgets_utils as widgets_utils
import cvplayer.core.utils.stylesheet_utils as stylesheet_utils
from PyQt6.QtGui import QKeySequence
from PyQt6.QtGui import QIcon
from pkg_resources import resource_filename

class PlayPauseButton(QToolButton):
    def __init__(self, video_player, layout, CSS='stylesheets/play_button.css', X=40, Y=40):
        super().__init__()
        self.start_button()
        widgets_utils.start_widget_basics(self, layout, CSS, fixed_width=X,fixed_height=Y)
        self.video_player = video_player
        self.pressed.connect(self.toggle) 
        self.video_player.started.connect(self.unlock)

    def toggle(self):
        if self.is_paused:
            self.is_paused = False
            self.setIcon(QIcon(resource_filename(__name__, 'icons/pause.png')))
            self.video_player.play_video()
        else:
            self.is_paused = True
            self.setIcon(QIcon(resource_filename(__name__, 'icons/play.png')))
            self.video_player.pause_video()
    
    def set_paused(self):
        self.setIcon(QIcon(resource_filename(__name__, 'icons/play.png')))
        self.is_paused = True 

    def start_button(self):
        self.setShortcut(QKeySequence('Space'))
        self.setAutoRaise(True)
        self.setIcon(QIcon(resource_filename(__name__, 'icons/play.png')))
        self.setIconSize(self.size())
        self.is_paused = True
        self.setEnabled(False)
        
    def unlock(self):
        self.setEnabled(True)

class NextFrameButton(QPushButton):
    def __init__(self, video_player, layout, X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Right'))
        widgets_utils.start_widget_basics(self, layout, fixed_width=X,fixed_height=Y)
        self.set_css()
        self.setEnabled(False)
        self.video_player = video_player
        self.pressed.connect(self.next_frame)
        self.video_player.started.connect(self.unlock)
        
    def next_frame(self):
        next_video_frame = self.video_player.video.current_frame_id + 1
        self.video_player.change_frame(next_video_frame)

    def unlock(self):
        self.setEnabled(True)

    def set_css(self):
        image_path = resource_filename(__name__, 'icons/next.png').replace("\\", "/")
        css_string = """
        QPushButton{
            border-image: url("""+image_path+""");
            background:transparent;    
        }
        QPushButton:hover {
            background-color: rgba(206, 197, 197, 0.21);
        }
        QPushButton:pressed{
            background-color: rgba(132, 129, 129, 0.264);
        } """
        self.setStyleSheet(css_string)
class PreviousFrameButton(QPushButton):
    def __init__(self, video_player, layout, CSS = 'stylesheets/previous_frame_button.css',X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Left'))
        widgets_utils.start_widget_basics(self, layout, CSS, fixed_width=X,fixed_height=Y)
        self.set_css()
        self.video_player = video_player
        self.setEnabled(False)
        self.pressed.connect(self.previous_frame)
        self.video_player.started.connect(self.unlock)
    
    def previous_frame(self):
        previous_video_frame = self.video_player.video.current_frame_id - 1
        self.video_player.change_frame(previous_video_frame)

    def unlock(self):
        self.setEnabled(True)

    def set_css(self):
        image_path = resource_filename(__name__, 'icons/previous.png').replace("\\", "/")
        css_string = """
        QPushButton{
            border-image: url("""+image_path+""");
            background:transparent;    
        }
        QPushButton:hover {
            background-color: rgba(206, 197, 197, 0.21);
        }
        QPushButton:pressed{
            background-color: rgba(132, 129, 129, 0.264);
        } """
        self.setStyleSheet(css_string)