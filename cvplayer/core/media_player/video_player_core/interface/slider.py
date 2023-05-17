# from PyQt6 import QtCore
# from PyQt6 import QtWidgets
# from PyQt6.QtCore import Qt 

# #Credits for eyllanesc, thanks bro, for real.
# #His StackOverflow account -> https://stackoverflow.com/users/6622587/eyllanesc

# class VideoSlider(QtWidgets.QSlider):
#     def __init__(self, video_player, layout ,CSS='opencvplayer/stylesheets/video_slider.css'):
#         super().__init__()
#         self.setOrientation(Qt.Horizontal)
#         widgets_utils.start_widget_basics(self, layout, CSS)
#         self.video_player = video_player
#         self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
#         self.change_slider_limits(0, self.video_player.video.total_number_of_frames)
        
#     def mouseReleaseEvent(self, event):
#         super(VideoSlider, self).mouseReleaseEvent(event)
#         if event.button() == QtCore.Qt.LeftButton:
#             slider_value = self.pixel_pos_to_range_value(event.pos())
#             self.setValue(slider_value)
#             self.video_player.change_frame(slider_value)

#     def set_value(self, value):
#         self.setValue(value)

#     def change_slider_limits(self, min_value, max_value):
#         self.setMinimum(int(min_value))
#         self.setMaximum(int(max_value))

#     def pixel_pos_to_range_value(self, pos):
#         opt = QtWidgets.QStyleOptionSlider()
#         self.initStyleOption(opt)
#         gr = self.style().subControlRect(QtWidgets.QStyle.CC_Slider, opt, QtWidgets.QStyle.SC_SliderGroove, self)
#         sr = self.style().subControlRect(QtWidgets.QStyle.CC_Slider, opt, QtWidgets.QStyle.SC_SliderHandle, self)

#         if self.orientation() == QtCore.Qt.Horizontal:
#             sliderLength = sr.width()
#             sliderMin = gr.x()
#             sliderMax = gr.right() - sliderLength + 1
#         else:
#             sliderLength = sr.height()
#             sliderMin = gr.y()
#             sliderMax = gr.bottom() - sliderLength + 1;
#         pr = pos - sr.center() + sr.topLeft()
#         p = pr.x() if self.orientation() == QtCore.Qt.Horizontal else pr.y()
#         return QtWidgets.QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - sliderMin,
#                                                sliderMax - sliderMin, opt.upsideDown)

    



from PyQt6 import QtCore
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStyle
from PyQt6.QtCore import Qt 
import cvplayer.core.utils.widgets_utils as widgets_utils


#Credits for eyllanesc, thanks bro, for real.
#His StackOverflow account -> https://stackoverflow.com/users/6622587/eyllanesc

class VideoSlider(QtWidgets.QSlider):
    def __init__(self, video_player, layout ,CSS='stylesheets/video_slider.css'):
        super().__init__()
        self.setOrientation(Qt.Orientation.Horizontal)
        widgets_utils.start_widget_basics(self, layout, CSS)
        self.video_player = video_player
        self.set_range(self.video_player.video.total_number_of_frames)
        self.setEnabled(False)
        self.video_player.started.connect(self.unlock)

    def mousePressEvent(self, e):
        if e.button() != Qt.MouseButton.LeftButton or not self.isEnabled():
            return super().mousePressEvent(self, e)
        e.accept()
        x = e.pos().x()
        value = (self.maximum() - self.minimum()) * x / self.width() + self.minimum()
        self.setValue(int(value))
        self.video_player.change_frame(value)
        
    # def mouseReleaseEvent(self, event):
    #     super(VideoSlider, self).mouseReleaseEvent(event)
    #     if event.button() == QtCore.Qt.MouseButton.LeftButton:
    #         slider_value = self.pixel_pos_to_range_value(event.pos())
    #         self.video_player.set_video_time(slider_value)

    def set_range(self, duration):
        self.setMinimum(0)
        self.setMaximum(int(duration))

    def set_value(self, value):
        self.setValue(int(value))

    def unlock(self):
        self.setEnabled(True)