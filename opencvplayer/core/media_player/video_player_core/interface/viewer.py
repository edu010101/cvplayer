from PyQt6.QtWidgets import QLabel
import opencvplayer.core.utils.widgets_utils as widgets_utils
import opencvplayer.core.utils.video_utils as video_utils


class ImageViewer(QLabel):
    def __init__(self, layout, CSS='opencvplayer/stylesheets/image_viewer.css'):
        super().__init__()
        self.setScaledContents(True)  
        widgets_utils.start_widget_basics(self, layout, CSS)
        self.cv2_image = None    

    def show_cv2_image(self, cv2_image):
        QPixmap = video_utils.cv2_image_to_QPixmap(cv2_image)
        self.setPixmap(QPixmap)

# from PyQt5 import QtCore, QtGui, QtWidgets
# import time

# class ImageViewer(QtWidgets.QGraphicsView):
#     photoClicked = QtCore.pyqtSignal(QtCore.QPoint)
#     change_image_on_viewer = QtCore.pyqtSignal()
    
#     def __init__(self, layout, CSS=None):
#         super(ImageViewer, self).__init__()
#         widgets_utils.start_widget_basics(self, layout, CSS)
#         self.cv2_image = None
        
#         self._zoom = 0
#         self._empty = True
#         self._scene = QtWidgets.QGraphicsScene(self)
#         self._photo = QtWidgets.QGraphicsPixmapItem()
#         self._scene.addItem(self._photo)
#         self.setScene(self._scene)
#         self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
#         self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
#         self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
#         self.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.change_image_on_viewer.connect(self.setPhoto)

#     def show_cv2_image(self, cv2_image):
#         self.QPixmap = video_utils.cv2_image_to_QPixmap(cv2_image)
#         self.change_image_on_viewer.emit()

#     def hasPhoto(self):
#         return not self._empty

#     def fitInView(self, scale=True):
#         rect = QtCore.QRectF(self._photo.pixmap().rect())
#         self.setSceneRect(rect)
#         unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
#         self.scale(1 / unity.width(), 1 / unity.height())
#         viewrect = self.viewport().rect()
#         scenerect = self.transform().mapRect(rect)
#         factor = min(viewrect.width() / scenerect.width(),
#                         viewrect.height() / scenerect.height())
#         self.scale(factor, factor)
#         self._zoom = 0

#     def setPhoto(self):
#         start = time.time()
#         self._zoom = 0
#         self._empty = False
#         self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
#         self._photo.setPixmap(self.QPixmap)
       
#         self.fitInView()
#         end = time.time()
#         print("Time to set photo: ", end - start)

#     def wheelEvent(self, event):
#         if self.hasPhoto():
#             if event.angleDelta().y() > 0:
#                 factor = 1.25
#                 self._zoom += 1
#             else:
#                 factor = 0.8
#                 self._zoom -= 1
#             if self._zoom > 0:
#                 self.scale(factor, factor)
#             elif self._zoom == 0:
#                 self.fitInView()
#             else:
#                 self._zoom = 0

#     def toggleDragMode(self):
#         if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
#             self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
#         elif not self._photo.pixmap().isNull():
#             self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

#     def mousePressEvent(self, event):
#         if self._photo.isUnderMouse():
#             self.photoClicked.emit(self.mapToScene(event.pos()).toPoint())
#         super(ImageViewer, self).mousePressEvent(event)


