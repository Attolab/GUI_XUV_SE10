from pyqtgraph import LinearRegionItem
from PySide6.QtCore import Signal,Qt
from PySide6.QtGui import QColor,QBrush

class CustomLinearRegionItem(LinearRegionItem):
    leftDoubleClicked = Signal(object)
    singleMiddleClicked = Signal(object)
    def mouseDoubleClickEvent(self,ev):
     if ev.button() == Qt.MouseButton.LeftButton:
            ev.accept()
            # self.moving = False
            self.leftDoubleClicked.emit(self)
    #  elif ev.button() == Qt.MouseButton.RightButton:
    #         ev.accept()
    #         # self.moving = False
    #         self.leftDoubleClicked.emit(self)
    def mouseClickEvent(self, ev):
        if self.moving and ev.button() == Qt.MouseButton.RightButton:
            ev.accept()
            for i, l in enumerate(self.lines):
                l.setPos(self.startPositions[i])
            self.moving = False
            self.sigRegionChanged.emit(self)
            self.sigRegionChangeFinished.emit(self)
            print('Got clicked')            
        if ev.button() == Qt.MouseButton.MiddleButton:
            ev.accept()
            self.singleMiddleClicked.emit(self)

    def changeROIColor(self,status):
        if status == 'unselected':   
            color_base = QColor(0, 0, 255, 50)
            color_hover = QColor(0, 0, 255, 100)
        elif status == 'selected':
            color_base = QColor(0, 255, 0, 50)     
            color_hover = QColor(0, 255, 0, 100)
        brush = QBrush(color_base)
        hoverBrush = QBrush(color_hover)
        self.setBrush(brush)
        self.setHoverBrush(hoverBrush)
        self.setMouseHover(True)
        self.setMouseHover(False)

# class CustomLinearRegionItem(LinearRegionItem):
#     leftDoubleClicked = Signal(object)
#     singleMiddleClicked = Signal(object)
#     def mouseDoubleClickEvent(self,ev):
#      if ev.button() == Qt.MouseButton.LeftButton:
#             ev.accept()
#             # self.moving = False
#             self.leftDoubleClicked.emit(self)
#      elif ev.button() == Qt.MouseButton.RightButton:
#             ev.accept()
#             # self.moving = False
#             self.leftDoubleClicked.emit(self)
#     def mouseClickEvent(self, ev):
#         if self.moving and ev.button() == Qt.MouseButton.RightButton:
#             ev.accept()
#             for i, l in enumerate(self.lines):
#                 l.setPos(self.startPositions[i])
#             self.moving = False
#             self.sigRegionChanged.emit(self)
#             self.sigRegionChangeFinished.emit(self)
#             print('Got clicked')            
#         if ev.button() == Qt.MouseButton.MiddleButton:
#             ev.accept()
#             self.singleMiddleClicked.emit(self)

#     def changeROIColor(self,status):
#         if status == 'unselected':   
#             color_base = QColor(0, 0, 255, 50)
#             color_hover = QColor(0, 0, 255, 100)
#         elif status == 'selected':
#             color_base = QColor(0, 255, 0, 50)     
#             color_hover = QColor(0, 255, 0, 100)
#         brush = QBrush(color_base)
#         hoverBrush = QBrush(color_hover)
#         self.setBrush(brush)
#         self.setHoverBrush(hoverBrush)
#         self.setMouseHover(True)
#         self.setMouseHover(False)        