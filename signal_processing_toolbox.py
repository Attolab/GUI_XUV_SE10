from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,QSignalMapper,
    QMetaObject, QObject, QPoint, QRect,QObject,Slot,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QPushButton,
    QSizePolicy, QWidget)
from signal_processing_toolbox_ui import Ui_SignalProcessingToolbox
from widget_manipulation_class import WidgetDataExtraction


class SignalProcessingToolbox(Ui_SignalProcessingToolbox,QWidget):
    emitSettings = Signal(object)
    signal_Axis = Signal(str,float)
    signal_comboBox = Signal(str,int)

    def __init__(self,parent=None,item_list = []):
        super(Ui_SignalProcessingToolbox, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupUi(self)
        # Initialize class to initialize/extract values from relevant QWdiget
        self.widget_extraction = WidgetDataExtraction(self,self.makeList_QWidget())        
        # Fill values if input
        self.widget_extraction.initializeValues(item_list)
        # Update GUI according to input
        self.updateGUI()
        # Set up connections
        self.connectSignal()


    def makeList_QWidget(self):                
        return['inputAxis0Start_doubleSpinBox', 'inputAxis0End_doubleSpinBox', 
                        'inputAxis1Start_doubleSpinBox', 'inputAxis1End_doubleSpinBox',         
                        'removeBackground_comboBox','removeBackground_doubleSpinBox',
                        'interpolation_comboBox','interpolation_spinBox',
                        'FT_zeropadding_comboBox','FT_zeropadding_spinBox',
                        'FT_window_comboBox','FT_zeropaddingpower2_spinBox',
                        'outputAxisStart_doubleSpinBox','outputAxisEnd_doubleSpinBox',
                        'inputAxis0Mult_lineEdit','inputAxis1Mult_lineEdit',
                        'inputAxis0Add_doubleSpinBox','inputAxis1Add_doubleSpinBox',
                        'outputAxisMult_lineEdit',                                          
                        ]

    @Slot(str)
    def inputAxis_changed(self,value):        
        self.signal_Axis.emit(self.sender().objectName(),float(value))
    @Slot(int)
    def comboBox_changed(self,value):        
        self.signal_comboBox.emit(self.sender().objectName(),value)
    @Slot(int)
    def removeBackground_changed(self,value):        
        self.signal_comboBox.emit(self.sender().objectName(),value)
    @Slot(int)
    def FTwindow_changed(self,value):        
        self.signal_comboBox.emit(self.sender().objectName(),value)

    @Slot(int)
    def FTzeroPadding_changed(self,value):        
        self.signal_comboBox.emit(self.sender().objectName(),value)

    @Slot(int)
    def interpolationType_changed(self,value):        
        self.signal_comboBox.emit(self.sender().objectName(),value)
       
    @Slot(int)
    def interpolationNumber_changed(self,value):        
        self.signal_removeBackground.emit(value)

    @Slot(int)
    def FTzeroPaddingPower2_changed(self,value):        
        self.signal_removeBackground.emit(value)

    def connectSignal(self):    
        # Line Edit
        # self.inputAxis0Start_doubleSpinBox.valueChanged.connect(self.inputAxis_changed)
        # self.inputAxis0End_doubleSpinBox.valueChanged.connect(self.inputAxis_changed)
        # self.inputAxis1Start_doubleSpinBox.valueChanged.connect(self.inputAxis_changed)
        # self.inputAxis1End_doubleSpinBox.valueChanged.connect(self.inputAxis_changed)                     
        # self.interpolation_comboBox.currentIndexChanged.connect(self.comboBox_changed)
        # Line Edit
        self.inputAxis0Start_doubleSpinBox.valueChanged.connect(self.applySettings)
        self.inputAxis0End_doubleSpinBox.valueChanged.connect(self.applySettings)
        self.inputAxis0Mult_lineEdit.editingFinished.connect(self.applySettings)
        self.inputAxis0Add_doubleSpinBox.valueChanged.connect(self.applySettings)            
        self.inputAxis1Start_doubleSpinBox.valueChanged.connect(self.applySettings)
        self.inputAxis1End_doubleSpinBox.valueChanged.connect(self.applySettings)  
        self.inputAxis1Mult_lineEdit.editingFinished.connect(self.applySettings) 
        self.inputAxis1Add_doubleSpinBox.valueChanged.connect(self.applySettings)                 
        self.removeBackground_doubleSpinBox.valueChanged.connect(self.applySettings)
        self.interpolation_spinBox.valueChanged.connect(self.applySettings)
        self.FT_zeropadding_spinBox.valueChanged.connect(self.applySettings)
        self.FT_zeropaddingpower2_spinBox.valueChanged.connect(self.applySettings)                            
        self.outputAxisMult_lineEdit.editingFinished.connect(self.applySettings)

        self.outputAxisStart_doubleSpinBox.valueChanged.connect(self.applySettings)
        self.outputAxisEnd_doubleSpinBox.valueChanged.connect(self.applySettings)               
        # Combobox
        self.interpolation_comboBox.currentIndexChanged.connect(self.applySettings)
        self.interpolation_comboBox.currentIndexChanged.connect(self.updateGUI)
        self.removeBackground_comboBox.currentIndexChanged.connect(self.applySettings)
        self.removeBackground_comboBox.currentIndexChanged.connect(self.updateGUI)
        self.FT_window_comboBox.currentIndexChanged.connect(self.applySettings)                
        self.FT_zeropadding_comboBox.currentIndexChanged.connect(self.applySettings)
        self.FT_zeropadding_comboBox.currentIndexChanged.connect(self.updateGUI)

    def updateGUI(self):
        if self.removeBackground_comboBox.currentIndex() != 4:
            self.removeBackground_doubleSpinBox.setEnabled(False)
        else:
            self.removeBackground_doubleSpinBox.setEnabled(True)            
        if self.FT_zeropadding_comboBox.currentIndex() == 1:            
            self.FT_zeropaddingpower2_spinBox.setVisible(True)
        else:
            self.FT_zeropaddingpower2_spinBox.setVisible(False)
        if self.FT_zeropadding_comboBox.currentIndex() != 3:
            self.FT_zeropadding_spinBox.setEnabled(False)
        else:
            self.FT_zeropadding_spinBox.setEnabled(True)
        if self.interpolation_comboBox.currentIndex() != 0:
            self.interpolation_spinBox.setEnabled(True)
        else:
            self.interpolation_spinBox.setEnabled(False)            
        
    def applyandexitSettings(self):
        self.applySettings()
        self.exitSettings()

    def applySettings(self):
        self.checkSettings()
        self.emitSettings.emit(self.widget_extraction.extractValues()) 

    def checkSettings(self):
        self.inputAxis0Start_doubleSpinBox.setMaximum(self.inputAxis0End_doubleSpinBox.value()-self.inputAxis0Start_doubleSpinBox.singleStep())
        self.inputAxis0End_doubleSpinBox.setMinimum(self.inputAxis0Start_doubleSpinBox.value()+self.inputAxis0End_doubleSpinBox.singleStep()) 
        self.inputAxis1Start_doubleSpinBox.setMaximum(self.inputAxis1End_doubleSpinBox.value()-self.inputAxis1Start_doubleSpinBox.singleStep())
        self.inputAxis1End_doubleSpinBox.setMinimum(self.inputAxis1Start_doubleSpinBox.value()+self.inputAxis1End_doubleSpinBox.singleStep())  
        self.outputAxisStart_doubleSpinBox.setMaximum(self.outputAxisEnd_doubleSpinBox.value()-self.outputAxisStart_doubleSpinBox.singleStep())
        self.outputAxisEnd_doubleSpinBox.setMinimum(self.outputAxisStart_doubleSpinBox.value()+self.outputAxisEnd_doubleSpinBox.singleStep())                    

    def updateAxisSettings(self,parameters):
        axis_lower = parameters[0]
        axis_upper = parameters[1]
        axis = parameters[2]
        steps = (axis[-1]-axis[0])/100        
        getattr(self,axis_lower).blockSignals(not(self.outputAxisEnd_doubleSpinBox.signalsBlocked()))
        getattr(self,axis_lower).setMinimum(axis[0])
        getattr(self,axis_lower).setSingleStep(steps)        
        getattr(self,axis_lower).blockSignals(not(self.outputAxisEnd_doubleSpinBox.signalsBlocked()))        
        getattr(self,axis_upper).blockSignals(not(self.outputAxisEnd_doubleSpinBox.signalsBlocked()))
        getattr(self,axis_upper).setMaximum(axis[-1])
        getattr(self,axis_upper).setSingleStep(steps)
        getattr(self,axis_upper).blockSignals(not(self.outputAxisEnd_doubleSpinBox.signalsBlocked()))    

    def exitSettings(self):
        self.hide()


def main():
    import sys
    app = QApplication([])
    tools = SignalProcessingToolbox()
    tools.show()
    app.exec()
if __name__=="__main__":
    main()

