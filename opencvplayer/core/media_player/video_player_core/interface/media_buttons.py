from PyQt6.QtWidgets import QPushButton, QToolButton
import opencvplayer.core.utils.widgets_utils as widgets_utils
import opencvplayer.core.utils.stylesheet_utils as stylesheet_utils
from PyQt6.QtGui import QKeySequence
from PyQt6.QtGui import QIcon

class PlayPauseButton(QToolButton):
    def __init__(self, video_player, layout, CSS='opencvplayer/stylesheets/play_button.css', X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Space'))
        self.setAutoRaise(True)
        self.setIcon(QIcon('opencvplayer/icons/PlayIcon.png'))
        self.setIconSize(self.size())
        widgets_utils.start_widget_basics(self, layout, CSS, fixed_width=X,fixed_height=Y)
        self.video_player = video_player
        self.pressed.connect(self.toggle) 
        self.is_paused = True
        
    def toggle(self):
        if self.is_paused:
            self.is_paused = False
            self.setIcon(QIcon('opencvplayer/icons/PauseIcon.png'))
            self.video_player.play_video()
        else:
            self.is_paused = True
            self.setIcon(QIcon('opencvplayer/icons/PlayIcon.png'))
            #stylesheet_utils.set_style_sheet(self, self.play_css)
            self.video_player.pause_video()
    
    def set_play(self):
        self.is_paused = True
        #stylesheet_utils.set_style_sheet(self, self.play_css)       

class NextFrameButton(QPushButton):
    def __init__(self, video_player, layout, CSS ='opencvplayer/stylesheets/next_frame_button.css', X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Right'))
        widgets_utils.start_widget_basics(self, layout, CSS, fixed_width=X,fixed_height=Y)
        self.video_player =  video_player
        self.pressed.connect(self.next_frame)
    
    def next_frame(self):
        next_video_frame = self.video_player.video.current_frame_id + 1
        self.video_player.change_frame(next_video_frame)

class PreviousFrameButton(QPushButton):
    def __init__(self, video_player, layout, CSS = 'opencvplayer/stylesheets/previous_frame_button.css',X=40, Y=40):
        super().__init__()
        self.setShortcut(QKeySequence('Left'))
        widgets_utils.start_widget_basics(self, layout, CSS, fixed_width=X,fixed_height=Y)
        self.video_player = video_player
        self.pressed.connect(self.previous_frame)
    
    def previous_frame(self):
        previous_video_frame = self.video_player.video.current_frame_id - 1
        self.video_player.change_frame(previous_video_frame)

