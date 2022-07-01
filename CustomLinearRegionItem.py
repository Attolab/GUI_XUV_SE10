from pyqtgraph import LinearRegionItem
from PySide6.QtCore import Signal,Qt

class CustomLinearRegionItem(LinearRegionItem):
    doubleClicked = Signal(object)

    def mouseDoubleClickEvent(self,ev):
     if ev.button() == Qt.MouseButton.LeftButton:
            ev.accept()
            self.moving = False
            self.doubleClicked.emit(self)

    def mouseClickEvent(self, ev):
        if self.moving and ev.button() == Qt.MouseButton.RightButton:
            ev.accept()
            for i, l in enumerate(self.lines):
                l.setPos(self.startPositions[i])
            self.moving = False
            self.sigRegionChanged.emit(self)
            self.sigRegionChangeFinished.emit(self)
            print('Got clicked')            
