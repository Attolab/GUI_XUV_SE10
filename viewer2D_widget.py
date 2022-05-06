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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,QTransform,QAction,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QPushButton,
    QSizePolicy, QWidget, QFileDialog,QMenu)
import pyqtgraph as pg
from viewer2D_widget_ui import Ui_Viewer2DWidget
import numpy as np


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

    def setupHistItem(self,layout,image,row = None, col = None):
        hist = pg.HistogramLUTItem(gradientPosition="left")
        hist.gradient.setColorMap(pg.colormap.get('hot', source='matplotlib'))
        layout.addItem(hist,row = row, col = col)
        hist.setImageItem(image)   
        hist.autoHistogramRange()
        return hist

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
        self.clearAll_pushButton.pressed.connect(self.clearROI)
        self.showROI_checkBox.pressed.connect(self.updateGUI)
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
        self.connect(tool_btn_menu.addAction("Add ROI"),SIGNAL("triggered()"), self.addROIh_menuFunction)
        self.connect(tool_btn_menu.addAction("Add ROI (horizontal)"),SIGNAL("triggered()"), self.addROIh_menuFunction) 
        self.connect(tool_btn_menu.addAction("Add ROI (vertical)"),SIGNAL("triggered()"), self.addROIv_menuFunction) 
        self.makeROI_toolButton.setMenu(tool_btn_menu)
        self.makeROI_toolButton.setDefaultAction(tool_btn_menu.actions()[0])
    def getScaling(self,input,total_length):        
        return (input[-1]-input[0])/total_length

    def getTransform(self,data,xaxis,yaxis):
        Q = QTransform()
        Q.translate(xaxis[0],yaxis[0])
        Q.scale(self.getScaling(xaxis,data.shape[0]),self.getScaling(yaxis,data.shape[1]))
        return Q

    def updateImage(self,item,data,xaxis,yaxis):
        item.setImage(data,autoRange=False)
        Q = self.getTransform(data,xaxis,yaxis)
        item.setTransform(Q)

    def updateView(self,view,xaxis,yaxis):
        offset_x = (xaxis[-1]-xaxis[0])/10
        offset_y = (yaxis[-1]-yaxis[0])/10
        view.setLimits(xMin = xaxis[0]-offset_x,xMax = xaxis[-1]+offset_x,yMin = yaxis[0]-offset_y,yMax = yaxis[-1]+offset_y)
        view.autoRange()

    def updateViewerWidget(self,mat_2D,x,y):
        self.updateImage(self.imageItem,mat_2D.T,x,y)
        self.updateView(self.view_2D,x,y)
        self.histLUT_2D._updateView()


    def addROIh_menuFunction(self):
        self.addROI_linearRegionItem(self.view_2D.viewRange()[1],'horizontal')

    def addROIv_menuFunction(self):        
        self.addROI_linearRegionItem(self.view_2D.viewRange()[0],'vertical')

    def makeInitialShape(self,size):      
        lengths = size*np.array([2,3])/5
        return lengths

    def addROI_linearRegionItem(self,edges,orientation):
        # lr = LinearRegionItem(self.makeInitialShape(np.diff(edges)),orientation=orientation,clipItem=self.imageItem)
        lr = pg.LinearRegionItem(self.makeInitialShape(np.diff(edges)),orientation=orientation,clipItem=self.imageItem)
        lr.setZValue(10)
        self.ROI.append(lr)
        self.plot_2D.addItem(self.ROI[-1])

    def clearROI(self):
        [self.removeROI(ROI) for ROI in self.ROI]

    def removeROI(self,item):
        self.plot_2D.removeItem(item) 
        self.ROI.remove(item)

    def getImageData(self):
        return self.imageItem.image
    
    def getImageShape(self):
        return self.getImageData().shape



# class LinearRegionItem(pg.LinearRegionItem):
#     def __init__(self, *args, **kwargs):
#         super(LinearRegionItem,self).__init__(*args, **kwargs)


#     def doStuff(self):
#         print('Doing stuff')

def main():
    import sys
    app = QApplication([])
    tof = Viewer2DWidget()
    tof.show()
    app.exec()

if __name__=="__main__":
    main()




    