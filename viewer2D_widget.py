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
from viewer2D_widget_ui import Ui_Viewer2DWidget
import numpy as np
import matplotlib.pyplot as plt


class Viewer2DWidget(Ui_Viewer2DWidget,QWidget):
    signal_importCurrentData = Signal()
    signal_importCustomData = Signal()
    def __init__(self,parent=None,name = 'Viewer2D'):
        super(Viewer2DWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        self.setupUi(self)
        self.label = pg.LabelItem(justify = "left")
        self.viewer_GraphicsLayoutWidget.addItem(self.label)
        self.plot_2D,self.view_2D,self.imageItem = self.setupImageWidget(self.viewer_GraphicsLayoutWidget,title=name,row = 0, col = 0)
        self.proxy = pg.SignalProxy(self.view_2D.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)     
        self.histLUT_2D = self.setupHistItem(self.viewer_GraphicsLayoutWidget,self.imageItem,row=0,col=1)
        # self.isoCurve = self.setupIsoCurveItem(self.imageItem)
        # self.isoLine = self.setupIsoLineItem(self.histLUT_2D)
        self.data = self.imageItem.image
        self.data_shape = self.data.shape
        self.ROI = []
        self.connectSignals()
        self.setupToolButton()
        self.updateGUI()


    # self.showIsoLine_checkBox.stateChanged.connect(self.updateGUI)
    # self.showHideWidget([self.isoCurve],self.showIsoLine_checkBox.isChecked())
    # def updateIsocurve(self):
    #     self.isoCurve.setLevel(self.isoLine.value())        
    # def setupIsoCurveItem(self,parent):
    #     # Isocurve drawing
    #     iso = pg.IsocurveItem(level=0.8, pen='g')
    #     iso.setParentItem(parent)
    #     iso.setZValue(5)
    #     iso.setData(pg.gaussianFilter(parent.image, (2, 2)))
    #     return iso


    # def setupIsoLineItem(self,parent):
    #     # Draggable line for setting isocurve level
    #     isoLine = pg.InfiniteLine(angle=0, movable=True, pen='g')
    #     parent.vb.addItem(isoLine)
    #     parent.vb.setMouseEnabled(y=False) # makes user interaction a little easier
    #     isoLine.setValue(self.isoCurve.level)
    #     isoLine.setZValue(1000) # bring iso line above contrast controls
    #     isoLine.sigDragged.connect(self.updateIsocurve)
    #     return isoLine


    def mouseMoved(self,evt):
        real_mousePoint = self.view_2D.mapSceneToView(evt[0])
        data = self.imageItem.image  # or use a self.data member
        nRows, nCols = data.shape 
        mousePoint = self.imageItem.mapFromScene(evt[0])
        row, col = int(mousePoint.x()), int(mousePoint.y())
        if (0 <= row < nRows) and (0 <= col < nCols):
            value = data[row, col]
            self.label.setText("<span style='font-size: 14pt; color: white'> x = %0.2f, <span style='color: white'> y = %0.2f</span>,<span style='color: white'> z = %0.2f</span>" % (real_mousePoint.x(), real_mousePoint.y(), value))
        else:
            self.label.setText('')


    def connectSignals(self):
        self.show2D_checkBox.stateChanged.connect(self.updateGUI)
        self.showHist_checkBox.stateChanged.connect(self.updateGUI)        
        self.showROI_checkBox.pressed.connect(self.updateGUI)
        # Table connection
        self.tableROI_tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableROI_tableWidget.connect(self.tableROI_tableWidget,SIGNAL("customContextMenuRequested(QPoint)" ), self.tableItemRightClicked)                        
        self.tableROI_tableWidget.itemSelectionChanged.connect(self.tableItemLeftClicked)


    def showHideWidget(self,items,show_bool = True):
        if show_bool:        
            [item.show() for item in items]
        else:
            [item.hide() for item in items]

    def updateGUI(self):
        self.showHideWidget([self.plot_2D],self.show2D_checkBox.isChecked())
        self.showHideWidget([self.histLUT_2D],self.showHist_checkBox.isChecked())
        self.showHideWidget(self.ROI,not(self.showROI_checkBox.isChecked()))


    def setupToolButton(self):        
        tool_btn_menu= QMenu(self)
        # self.connect(tool_btn_menu.addAction("Add ROI"),SIGNAL("triggered()"), self.addROI)
        self.connect(tool_btn_menu.addAction("Add ROI (H)"),SIGNAL("triggered()"), self.addROIh_menuFunction) 
        self.connect(tool_btn_menu.addAction("Add ROI (V)"),SIGNAL("triggered()"), self.addROIv_menuFunction) 
        self.makeROI_toolButton.setMenu(tool_btn_menu)
        self.makeROI_toolButton.setDefaultAction(tool_btn_menu.actions()[1])

##################################### IMAGE VIEW/ITEM ########################################

    def setupImageWidget(self,layout,title = '', row = None, col = None):
        plot = layout.addPlot(title=title,labels={'bottom': ('x axis title'), 'left': ('y axis title')},row = row, col = col)
        plot.ctrlMenu = None
        view = plot.getViewBox()
        img = pg.ImageItem()              
        data = np.random.normal(size=(200, 100))
        data[20:80, 20:80] += 2.
        data = pg.gaussianFilter(data, (3, 3))
        data += np.random.normal(size=(200, 100)) * 0.1                
        img.setImage(data,autoRange=True)
        plot.addItem(img)     
        return plot,view,img

    def setupHistItem(self,layout,image,row = None, col = None):
        hist = pg.HistogramLUTItem(gradientPosition="left")
        hist.gradient.setColorMap(pg.colormap.get('hot', source='matplotlib'))
        layout.addItem(hist,row = row, col = col)
        hist.setImageItem(image)   
        hist.autoHistogramRange()
        return hist
    def getScaling(self,input,total_length):        
        return (input[-1]-input[0])/total_length

    def getImageTransformParameters(self):
        scale_x = self.imageItem.transform().m11() # Image/Axis scaling
        offset_x = self.imageItem.transform().m31() # Axis offset
        scale_y = self.imageItem.transform().m22() # Image/Axis scaling
        offset_y = self.imageItem.transform().m32() # Axis offset      
        n_x,n_y = self.getImageData().shape # Length of non integrated axis
        return [(n_x,scale_x,offset_x),(n_y,scale_y,offset_y)]

    def makeTransform(self,data,xaxis,yaxis):
        Q = QTransform()
        Q.translate(xaxis[0],yaxis[0])
        Q.scale(self.getScaling(xaxis,data.shape[0]),self.getScaling(yaxis,data.shape[1]))
        return Q

    def updateImage(self,item,data,xaxis,yaxis):
        item.setImage(data,autoRange=False)
        item.setTransform(self.makeTransform(data,xaxis,yaxis))

    def updateView(self,view,xaxis,yaxis):
        offset_x = (xaxis[-1]-xaxis[0])/10
        offset_y = (yaxis[-1]-yaxis[0])/10
        view.setLimits(xMin = xaxis[0]-offset_x,xMax = xaxis[-1]+offset_x,yMin = yaxis[0]-offset_y,yMax = yaxis[-1]+offset_y)
        view.autoRange()

    def updateViewerWidget(self,mat_2D,x,y):
        self.updateImage(self.imageItem,mat_2D.T,x,y)
        self.updateView(self.view_2D,x,y)
        self.histLUT_2D._updateView()

    def getImageData(self):
        return self.imageItem.image
    
    def getImageShape(self):
        return self.getImageData().shape

    ################################################## ROI functions ##########################################    

    def addROIh_menuFunction(self):
        self.addROI_linearRegionItem(self.view_2D.viewRange()[1],'horizontal')

    def addROIv_menuFunction(self):        
        self.addROI_linearRegionItem(self.view_2D.viewRange()[0],'vertical')



    def addROI_linearRegionItem(self,edges,orientation):

        # Create ROI item
        lr = CustomLinearRegionItem(self.makeInitialShape(edges),orientation=orientation,clipItem=self.imageItem)        
        # lr = pg.LinearRegionItem(self.makeInitialShape(np.diff(edges)),orientation=orientation,clipItem=self.imageItem)        
        lr.leftDoubleClicked.connect(self.gotLeftDoubleClicked)
        lr.singleMiddleClicked.connect(self.gotMiddleSingleClicked)
        lr.setZValue(10)
        # Type of syntax to accept clicking on it
        # Store ROI item
        self.ROI.append(lr)
        # Show ROI item in viewer
        self.plot_2D.addItem(self.ROI[-1])   
        # Store ROI item in table
        self.addEntry_tableWidget(orientation=orientation)

    def makeInitialShape(self,edges):      
        lengths = edges[0] + np.diff(edges)*np.array([2,3])/5
        return lengths

    def gotMiddleSingleClicked(self,ROI_doubleclicked):
        print('I got destroyed')
        for index, ROI in enumerate(self.ROI): 
            if ROI_doubleclicked == ROI:
                self.removeROI(ROI)
                self.tableROI_tableWidget.removeRow(index)
                return

    def gotLeftDoubleClicked(self,ROI_doubleclicked):
        print('I got doubleclicked')
        for index, ROI in enumerate(self.ROI): 
            if ROI_doubleclicked == ROI:
                self.tableROI_tableWidget.selectRow(index)
                return
    def removeROI(self,item):
        self.plot_2D.removeItem(item) 
        self.ROI.remove(item)

    def changeROIColor(self,index,status):
        if status == 'unselected':   
            color_base = QColor(0, 0, 255, 50)
            color_hover = QColor(0, 0, 255, 100)
        elif status == 'selected':
            color_base = QColor(0, 255, 0, 50)     
            color_hover = QColor(0, 255, 0, 100)
        brush = QBrush(color_base)
        hoverBrush = QBrush(color_hover)
        if len(self.ROI) > index:
            self.ROI[index].setBrush(brush)
            self.ROI[index].setHoverBrush(hoverBrush)
            self.ROI[index].setMouseHover(True)
            self.ROI[index].setMouseHover(False)
    ################################################## Table widget functions ##########################################    
    def get_selectedRows(self,sender):
        return np.unique([sender.row(item) for item in sender.selectedItems()])

    def addEntry_tableWidget(self,name=None,orientation='H'):
        nRow = self.tableROI_tableWidget.rowCount()        
        # Add a new entry to listWidget
        self.tableROI_tableWidget.insertRow(nRow)
        if not(name):
            name = f'{nRow}'          
        if orientation == 'horizontal':
            orientation ='H'
        elif orientation == 'vertical':
            orientation ='V'
        item = QTableWidgetItem(name)
        item.setFlags(item.flags() | Qt.ItemIsEditable)    
        self.tableROI_tableWidget.setItem(nRow,0,item)
        item = QTableWidgetItem(orientation)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)        
        self.tableROI_tableWidget.setItem(nRow,1,item)
        self.tableROI_tableWidget.clearSelection()
        self.tableROI_tableWidget.setCurrentItem(item)   

    def tableItemLeftClicked(self):
        row_sel = self.get_selectedRows(self.tableROI_tableWidget)
        # row_sel = np.unique([self.tableROI_tableWidget.row(item) for item in self.tableROI_tableWidget.selectedItems()])
        for row in np.arange(self.tableROI_tableWidget.rowCount()):
            if row in row_sel:
                self.changeROIColor(row,'selected')            
            else:
                self.changeROIColor(row,'unselected')            

    def tableItemRightClicked(self, QPos): 
        sender = self.sender()
        self.roiMenu= QMenu(self)
        self.roiOperationMenu = QMenu('Operation',self)
        self.roiMenu.addMenu(self.roiOperationMenu)
        # show_button = QAction("Show Item(s)", self.roiMenu)
        # show_button.setCheckable(True)
        # show_button.setChecked(True)
        # connect(show_button, SIGNAL("triggered()"), this, SLOT(slot_SomethingChecked()));
        # show_button = QAction("Show Sum", self.roiOperationMenu) Qmenu_tableOperationFindCOM
        self.connect(self.roiOperationMenu.addAction("COM ROI"),SIGNAL("triggered()"), lambda who=sender: self.Qmenu_tableOperationFindCOM(who)) 
        self.connect(self.roiOperationMenu.addAction("Sum ROI"),SIGNAL("triggered()"), lambda who=sender: self.Qmenu_tableOperationSum(who)) 
        self.connect(self.roiOperationMenu.addAction("Find Max"),SIGNAL("triggered()"), lambda who=sender: self.Qmenu_tableOperationFindMax(who)) 
        self.connect(self.roiMenu.addAction("Remove Item(s)"),SIGNAL("triggered()"), lambda who=sender: self.Qmenu_tableRemoveItemClicked(who)) 
        self.connect(self.roiMenu.addAction("Clear all"),SIGNAL("triggered()"), lambda who=sender: self.Qmenu_tableClearClicked(who)) 
        
        parentPosition = sender.mapToGlobal(QPoint(0, 0))        
        self.roiMenu.move(parentPosition + QPos)
        self.roiMenu.show()   

    def removeEntry_table(self,row,sender):
        # Remove entry in table
        sender.removeRow(row)
    def removeSelectedItems_table(self,sender):
        # Remove all selected items
        row_sel = np.flip(np.unique([sender.row(item) for item in sender.selectedItems()]))
        for row in row_sel:
            self.removeROI(self.ROI[row])
            self.removeEntry_table(row,sender)           

    def clearTable(self,sender):    
        # Remove all items    
        for row in np.flip(np.arange(sender.rowCount())):
            self.removeROI(self.ROI[row])
            self.removeEntry_table(row,sender)   
        # [self.removeEntry_table(sender.item(row),sender) for row in np.flip(np.arange(sender.count()))]    

    ################################################## List widget functions ##########################################        

    # def addEntry(self,item):
    #     # Add a new entry to listWidget
    #     item.setFlags(item.flags() | Qt.ItemIsEditable)
    #     self.listROI_listWidget.addItem(item)
    #     self.listROI_listWidget.clearSelection()
    #     self.listROI_listWidget.setCurrentItem(item)   

    # def listItemLeftClicked(self,current_item,old_item):
    #     self.changeROIColor(self.listROI_listWidget.row(current_item),'selected')
    #     self.changeROIColor(self.listROI_listWidget.row(old_item),'unselected')

    # def listItemRightClicked(self, QPos): 
    #     sender = self.sender()
    #     self.roiMenu= QMenu(self)
    #     self.connect(self.roiMenu.addAction("Remove Item(s)"),SIGNAL("triggered()"), lambda who=sender: self.Qmenu_listRemoveItemClicked(who)) 
    #     self.connect(self.roiMenu.addAction("Clear all"),SIGNAL("triggered()"), lambda who=sender: self.Qmenu_listClearClicked(who)) 
    #     parentPosition = sender.mapToGlobal(QPoint(0, 0))        
    #     self.roiMenu.move(parentPosition + QPos)
    #     self.roiMenu.show()

    # def removeEntry_list(self,item,sender):
    #     # Remove entry in list
    #     sender.takeItem(sender.row(item))

    # def removeSelectedItems_list(self,sender):
    #     # Remove all selected items
    #     [self.removeEntry_list(item,sender) for item in sender.selectedItems()]        

    # def clearList(self,sender):    
    #     # Remove all items    
    #     [self.removeEntry_list(sender.item(row),sender) for row in np.flip(np.arange(sender.count()))]    



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

    def Qmenu_tableOperationFindCOM(self,sender) :
        image_parameters = self.getImageTransformParameters()
        for row in self.get_selectedRows(self.tableROI_tableWidget):
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

    def Qmenu_tableOperationFindMax(self,sender) :
        image_parameters = self.getImageTransformParameters()        
        for row in self.get_selectedRows(self.tableROI_tableWidget):
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
            
    def Qmenu_tableOperationSum(self,sender) :
        image_parameters = self.getImageTransformParameters()
        for row in self.get_selectedRows(self.tableROI_tableWidget):
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


    def Qmenu_tableRemoveItemClicked(self,sender):
        self.removeSelectedItems_table(sender)

    def Qmenu_tableClearClicked(self,sender):
        self.clearTable(sender)     

    ################################################## Context menu functions ##########################################    
    def Qmenu_listRemoveItemClicked(self,sender):
        self.removeSelectedItems_list(sender)

    def Qmenu_listClearClicked(self,sender):
        self.clearList(sender)     

def main():
    import sys
    app = QApplication([])
    tof = Viewer2DWidget()
    tof.show()
    app.exec()

if __name__=="__main__":
    main()




    