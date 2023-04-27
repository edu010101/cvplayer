from PyQt6.QtWidgets import QPushButton
import cvplayer.core.utils.widgets_utils as widgets_utils
from PyQt6.QtGui import QKeySequence

class NextImageButton(QPushButton):
    def __init__(self, image_player, layout, CSS ='cvplayer/stylesheets/next_frame_button.css', X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Right'))
        widgets_utils.start_widget_basics(self, layout, CSS, fixed_width=X,fixed_height=Y)
        self.image_player =  image_player
        self.pressed.connect(self.next_image)
    
    def next_image(self):
        #next_video_frame = self.video_player.video.current_frame_id + 1
        #self.image_player.change_frame(next_video_frame)
        pass
class PreviousImageButton(QPushButton):
    def __init__(self, image_player, layout, CSS = 'cvplayer/stylesheets/previous_frame_button.css',X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Left'))
        widgets_utils.start_widget_basics(self, layout, CSS, fixed_width=X,fixed_height=Y)
        self.image_player = image_player
        self.pressed.connect(self.previous_image)
    
    def previous_image(self):
        #previous_video_frame = self.image_player.video.current_frame_id - 1
        #self.image_player.change_frame(previous_video_frame)
        pass
