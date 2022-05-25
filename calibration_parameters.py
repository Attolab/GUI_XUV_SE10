from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,QRegularExpression,
    QMetaObject, QObject, QPoint, QRect,Signal,SIGNAL,QFile,QDataStream,QFileInfo,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,QRegularExpressionValidator,
    QFont, QFontDatabase, QGradient, QIcon,QTransform,QAction,QDoubleValidator,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QPushButton,QFileDialog,
    QTableWidgetItem,QStyledItemDelegate,QLineEdit,
    QSizePolicy, QWidget,QMenu)

from calibration_parameters_ui import Ui_Calibration_parameters
from widget_manipulation_class import WidgetDataExtraction

class Calibration_parameters(Ui_Calibration_parameters, QWidget):

    emitParameters = Signal(object)

    def __init__(self, parent=None, item_list = []):
        super(Calibration_parameters, self).__init__(parent)
        self.setupUi(self)
        self.widget_extraction = WidgetDataExtraction(self,self.makeList_QWidget()) 
        self.widget_extraction.initializeValues(item_list)
        self.connectSignal()
    
    def makeList_QWidget(self):
        return ["inputAxis0Mult_lineEdit_2", "inputAxis0Mult_lineEdit", "inputAxis0Mult_lineEdit_3"]
    
    def connectSignal(self):
        self.inputAxis0Mult_lineEdit_2.editingFinished.connect(self.applyParameters)
        self.inputAxis0Mult_lineEdit.editingFinished.connect(self.applyParameters)
        self.inputAxis0Mult_lineEdit_3.editingFinished.connect(self.applyParameters)
    
    def applyParameters(self):
        self.emitParameters.emit(self.widget_extraction.extractValues())

def main():
    app = QApplication([])
    calib = Calibration_parameters()
    calib.show()
    app.exec()

if __name__=="__main__":
    main()