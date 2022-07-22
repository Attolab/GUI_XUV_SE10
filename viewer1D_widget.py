##############################################################################
##
# This file is part of pymepixviewer
#
# https://arxiv.org/abs/1905.07999
#
#
# pymepixviewer is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pymepixviewer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pymepixviewer.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from turtle import Pen
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,SIGNAL,Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,QAction,
    QFont, QFontDatabase, QGradient, QIcon,QTransform,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QPushButton,QListWidgetItem,QTableWidgetItem,
    QSizePolicy, QWidget, QFileDialog,QMenu)
import pyqtgraph as pg
from CustomLinearRegionItem import CustomLinearRegionItem
from viewer1D_widget_ui import Ui_Viewer1DWidget
import numpy as np
import matplotlib.pyplot as plt


class Viewer1DWidget(Ui_Viewer1DWidget,QWidget):
    signal_importCurrentData = Signal()
    signal_importCustomData = Signal()
    def __init__(self,parent=None,name = 'Viewer1D'):
        super(Viewer1DWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupUi(self)
        self.ROI = []
        self.plot_list = []        
        self.label = pg.LabelItem(justify = "left")
        self.viewer_GraphicsLayoutWidget.addItem(self.label)



        self.viewer_GraphicsLayoutWidget.scene().sigMouseClicked.connect(self.onClick)
        
        self.plot,self.view_1D = self.setupPlotWidget(self.viewer_GraphicsLayoutWidget,title=name,row = 0, col = 0)
        self.proxy = pg.SignalProxy(self.view_1D.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)     
        self.connectSignals()
        self.setupToolButton()
        self.updateGUI()    
        self.addPlot_pushButton.clicked.connect(self.addPlot)
    def onClick(self,event):
        items = self.viewer_GraphicsLayoutWidget.scene().items(event.scenePos())
        print( "Plots:", [x for x in items if isinstance(x, pg.PlotCurveItem)])
        [x for x in items if isinstance(x, pg.PlotCurveItem)]
        if pg.PlotCurveItem in items:
            print(0)
            # print("Items:",[x for x in items])

    def addPlot(self,name = None, x = np.arange(1000),y = None):        
        if y is None:
            y = np.random.normal(0,100)+np.random.normal(size=(1000,))
        plot_dataItem = pg.PlotDataItem(x,y)
        color_plot = pg.intColor(len(self.plot_list))
        plot_dataItem.setPen(color_plot)
        plot_dataItem.setCurveClickable(True,width = 3)
        plot_dataItem.sigClicked.connect(self.plotDataGotClicked)
        self.plot.addItem(plot_dataItem)
        self.plot_list.append(plot_dataItem)
        self.tablePlot_tableWidget.addEntry(name = name,color=color_plot)


    def plotDataGotClicked(self,ev): 
        self.tablePlot_tableWidget.setCurrentCell([i for i in range(len(self.plot_list)) if self.plot_list[i] == ev][0],0)
    def setupPlotWidget(self,layout,title = '', row = None, col = None):
        plot = layout.addPlot(title=title,labels={'bottom': ('x axis title'), 'left': ('y axis title')},row = row, col = col)
        plot.ctrlMenu = None
        # plot.setMenuEnabled(False,enableViewBoxMenu='same')
        view = plot.getViewBox()
        return plot,view

    def mouseMoved(self,evt):
        mousePoint = self.plot.vb.mapSceneToView(evt[0])
        self.label.setText("<span style='font-size: 14pt; color: white'> x = %0.2f, <span style='color: white'> y = %0.2f</span>" % (mousePoint.x(), mousePoint.y()))


    def connectSignals(self):     
        self.showROI_checkBox.pressed.connect(self.updateGUI)
        # Table connection
        self.tablePlot_tableWidget.itemSelected_signal.connect(self.updatPlotSelection)
        # self.tablePlot_tableWidget.QMenu_signal.connect(self.sendQMenuCommand)
        self.tablePlot_tableWidget.removeItem_signal.connect(self.removePlotTableItem)        
        # Table connection
        self.tableROI_tableWidget.itemSelected_signal.connect(self.updateROISelection)
        self.tableROI_tableWidget.QMenu_signal.connect(self.sendQMenuCommand)
        self.tableROI_tableWidget.removeItem_signal.connect(self.removeROITableItem)

        self.tablePlot_tableWidget.checkBox_signal.connect(self.showPlot)
        self.tablePlot_tableWidget.colorButton_signal.connect(self.colorPlot)

    def colorPlot(self,color,row):
        self.plot_list[row].setPen(color)
        if row in self.tablePlot_tableWidget.get_selectedRows():
            self.plot_list[row].setShadowPen(pg.mkPen(self.tablePlot_tableWidget.getColorButton(row), width=2, cosmetic=True))

    def showPlot(self,status,row):
        if status:
            self.plot_list[row].show()
        else:
            self.plot_list[row].hide()

    def showHideWidget(self,items,show_bool = True):
        if show_bool:        
            [item.show() for item in items]
        else:
            [item.hide() for item in items]

    def updateGUI(self):
        self.showHideWidget(self.ROI,not(self.showROI_checkBox.isChecked()))

    def setupToolButton(self):        
        tool_btn_menu= QMenu(self)
        self.connect(tool_btn_menu.addAction("Add ROI (H)"),SIGNAL("triggered()"), self.addROIh_menuFunction) 
        self.connect(tool_btn_menu.addAction("Add ROI (V)"),SIGNAL("triggered()"), self.addROIv_menuFunction) 
        self.makeROI_toolButton.setMenu(tool_btn_menu)
        self.makeROI_toolButton.setDefaultAction(tool_btn_menu.actions()[1])

    def updateView(self,view,xaxis,yaxis):
        offset_x = (xaxis[-1]-xaxis[0])/10
        offset_y = (yaxis[-1]-yaxis[0])/10
        view.setLimits(xMin = xaxis[0]-offset_x,xMax = xaxis[-1]+offset_x,yMin = yaxis[0]-offset_y,yMax = yaxis[-1]+offset_y)
        view.autoRange()

    def updateViewerWidget(self,x,y):
        self.updateView(self.view_1D,x,y)

    ################################################## ROI functions ##########################################    
    def addROIh_menuFunction(self):
        self.addROI_linearRegionItem(self.view_1D.viewRange()[1],'horizontal')

    def addROIv_menuFunction(self):        
        self.addROI_linearRegionItem(self.view_1D.viewRange()[0],'vertical')

    def addROI_linearRegionItem(self,edges,orientation):
        # Create ROI item
        lr = CustomLinearRegionItem(self.makeInitialShape(edges),orientation=orientation,clipItem=self.imageItem)        
        lr.leftDoubleClicked.connect(self.gotLeftDoubleClicked)
        lr.singleMiddleClicked.connect(self.gotMiddleSingleClicked)
        lr.setZValue(10)
        # Store ROI item
        self.ROI.append(lr)
        # Show ROI item in viewer
        self.plot.addItem(self.ROI[-1])   
        # Store ROI item in table
        self.tableROI_tableWidget.addEntry(orientation=orientation)

    def makeInitialShape(self,edges):      
        lengths = edges[0] + np.diff(edges)*np.array([2,3])/5
        return lengths

    def gotMiddleSingleClicked(self,ROI_clicked):
        print('I got destroyed')
        for index, ROI in enumerate(self.ROI): 
            if ROI_clicked == ROI:
                self.removeROI(ROI)
                self.tableROI_tableWidget.removeRow(index)
                return
    def gotLeftDoubleClicked(self,ROI_clicked):
        print('I got doubleclicked')
        for index, ROI in enumerate(self.ROI): 
            if ROI_clicked == ROI:
                self.tableROI_tableWidget.selectRow(index)
                return

    def removePlot(self,item):
        self.plot.removeItem(item) 
        self.plot_list.remove(item)
    def removePlotTableItem(self,row):
        self.removePlot(self.plot_list[row])

    def updatPlotSelection(self,row,status):    
        if len(self.plot_list) > row:
            if status == 'unselected':   
                self.plot_list[row].setShadowPen(None)
            elif status == 'selected':
                self.plot_list[row].setShadowPen(pg.mkPen(self.tablePlot_tableWidget.getColorButton(row), width=2, cosmetic=True))

    def removeROI(self,item):
        self.plot.removeItem(item) 
        self.ROI.remove(item)

    def updateROISelection(self,row,status):
        if len(self.ROI) > row:
            self.ROI[row].changeROIColor(status)
    def removeROITableItem(self,row):
        self.removeROI(self.ROI[row])

    ################################################## Context menu functions ##########################################  
    def axisToIndex(self,axis,scale,offset):
        return int((axis-offset)/scale)
    def indexToAxis(self,index,scale,offset):        
        return (index*scale+offset)

    def getImageRegion(self,edges,orientation,parameters):
        axis_plot = self.makeAxis(parameters)       
        if orientation == 'H':
            l_b,h_b = [self.axisToIndex(edge,parameters[1][1],parameters[1][2]) for edge in edges]
            ROI_zone = self.getImageData()[:,l_b:h_b]
            axis_plot[1] = axis_plot[1][np.logical_and(axis_plot[1] >= edges[0],axis_plot[1] <= edges[1])]
        elif orientation == 'V':
            l_b,h_b = [self.axisToIndex(edge,parameters[0][1],parameters[0][2]) for edge in edges]
            ROI_zone = self.getImageData()[l_b:h_b,:]
            axis_plot[0] = axis_plot[0][np.logical_and(axis_plot[0] >= edges[0],axis_plot[0] <= edges[1])]
        return ROI_zone,axis_plot
    
    def getAxis(self):
        return self.makeAxis(self.getImageTransformParameters())

    def makeAxis(self,parameters):
        axis = []
        for parameter in parameters:
            n,scale,offset = parameter
            axis.append(np.arange(n)*scale+offset)
        return axis

    def getOrientationIndex(self,orientation):
        if orientation == 'H':
            return 0
        elif orientation == 'V':
            return 1


    def sendQMenuCommand(self,command):
        if command == 'COM':
            self.getCOM()
        elif command == 'Sum':
            self.getSum()
        elif command == 'Max':            
            self.getMax()
        elif command == 'Min':            
            self.getMin()

    def getCOM(self):
        image_parameters = self.getImageTransformParameters()
        for row in self.tableROI_tableWidget.get_selectedRows():
            orientation = self.tableROI_tableWidget.item(row,1).text()
            image_ROI,axis_plot = self.getImageRegion(self.ROI[row].getRegion(),orientation,image_parameters)
            if orientation == 'H':
                xAxis_plot = axis_plot[0]
                max_ROI = axis_plot[1][np.argmax(image_ROI,axis=1)]
            elif orientation == 'V':     
                xAxis_plot = axis_plot[1]       
                max_ROI = axis_plot[0][np.argmax(image_ROI,axis=0)]
            plt.plot(xAxis_plot,max_ROI,label=self.tableROI_tableWidget.item(row,0).text)
        plt.show() 
          
    def getMax(self) :
        image_parameters = self.getImageTransformParameters()        
        for row in self.tableROI_tableWidget.get_selectedRows():
            orientation = self.tableROI_tableWidget.item(row,1).text()
            image_ROI,axis_plot = self.getImageRegion(self.ROI[row].getRegion(),orientation,image_parameters)
            if orientation == 'H':
                xAxis_plot = axis_plot[0]
                max_ROI = axis_plot[1][np.argmax(image_ROI,axis=1)]
            elif orientation == 'V':     
                xAxis_plot = axis_plot[1]       
                max_ROI = axis_plot[0][np.argmax(image_ROI,axis=0)]
            plt.plot(xAxis_plot,max_ROI,label=self.tableROI_tableWidget.item(row,0).text)
        plt.show()    
            
    def getSum(self) :
        image_parameters = self.getImageTransformParameters()
        for row in self.tableROI_tableWidget.get_selectedRows():
            orientation = self.tableROI_tableWidget.item(row,1).text()
            image_ROI,axis_plot = self.getImageRegion(self.ROI[row].getRegion(),orientation,image_parameters)
            if orientation == 'H':
                xAxis_plot = axis_plot[0]                
                sum_ROI = np.sum(image_ROI,axis=1)
            elif orientation == 'V':    
                xAxis_plot = axis_plot[1]        
                sum_ROI = np.sum(image_ROI,axis=0)
            plt.plot(xAxis_plot,sum_ROI,label=self.tableROI_tableWidget.item(row,0).text)
        plt.show()


def main():
    import sys
    app = QApplication([])
    tof = Viewer1DWidget()
    tof.show()
    app.exec()

if __name__=="__main__":
    main()




    