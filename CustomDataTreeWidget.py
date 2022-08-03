
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,SIGNAL,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,QAction,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QTreeWidget,QTreeWidgetItem,
    QVBoxLayout, QWidget,QTableWidgetItem,QFileDialog,QDockWidget,QMainWindow,QHeaderView)
from CustomDataTreeWidget_ui import Ui_CustomDataTreeWidget
from CustomTableWidget import CustomTableWidget,fileSelectionTableWidget
from pyqtgraph import DataTreeWidget
import numpy as np

class CustomDataTreeWidget(Ui_CustomDataTreeWidget,QWidget):
    showVariable_signal = Signal(object)
    """Tab Widget that that can have new tabs easily added to it."""
    def __init__(self,parent = None,data = None):
        super(CustomDataTreeWidget, self).__init__(parent) 
        self.setupUi(self)
        self.connectSignals()  
        if data:
            self.addEntry(data)

    def connectSignals(self):
        self.add_pushButton.pressed.connect(self.addEntry_pushButton)
        self.delete_pushButton.pressed.connect(self.removeEntry_pushButton)
        self.data_treeWidget.itemDoubleClicked.connect(self.doubleClicked_treeWidget_function)

    def addEntry_pushButton(self):
        data = {"Project A": np.ones((5,1)),
                "Project B": np.zeros((5,1)),
                "Project C": np.ones((5,1))}   
        self.addEntry(data)

    def addEntry(self,data=None):
        items = []
        for key, values in data.items():
            item = QTreeWidgetItem([key])
            name = key
            desc = "shape=%s dtype=%s" % (values.shape, values.dtype)
            typeStr = type(values).__name__
            item = QTreeWidgetItem([name, typeStr,desc])
            # item.addChild(child)
            items.append(item)
        self.data_treeWidget.insertTopLevelItems(0, items) 
        [self.data_treeWidget.resizeColumnToContents(col) for col in range(self.data_treeWidget.columnCount())]
    def removeEntry(self,item):
        self.data_treeWidget.takeTopLevelItem(self.data_treeWidget.indexOfTopLevelItem(item))
        # self.data_treeWidget.indexOfTopLevelItem(item)

    def removeEntry_pushButton(self):
        [self.removeEntry(item) for item in self.data_treeWidget.selectedItems()]
        
    def doubleClicked_treeWidget_function(self,item):
        self.showVariable_signal.emit(item.text(0))
        print(item.text(0))



def main():
    import numpy as np
    data = {"Project A": np.ones((5,1)),
            "Project B": np.zeros((5,1)),
            "Project C": np.ones((5,1))}    
    import sys
    app = QApplication(['test'])
    tof = CustomDataTreeWidget(data = data)
    tof.show()
    app.exec()

if __name__=="__main__":
    main()


