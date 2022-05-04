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
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,QTransform,QAction,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QCloseEvent)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QPushButton,
    QSizePolicy, QWidget, QFileDialog,QMenu)
import pyqtgraph as pg
from viewer_widget_ui import Ui_ViewerWidget
import numpy as np


class ViewerWidget(Ui_ViewerWidget,QWidget):
    def __init__(self,parent=None,name='Viewer1D'):
        super(ViewerWidget, self).__init__(parent)
        # Set up the user interface from Designer.        
        self.setupUi(self)
        self.connectSignals()
        # self.label = pg.TextItem()
        self.label = pg.LabelItem(justify = "left")
        self.viewer_GraphicsLayoutWidget.addItem(self.label)
        self.plot_2D,self.view_2D,self.imageItem = self.setupImageWidget(self.viewer_GraphicsLayoutWidget,title=name,row = 0, col = 0)
        self.proxy = pg.SignalProxy(self.view_2D.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)     
        self.histLUT_2D = self.setupHistItem(self.viewer_GraphicsLayoutWidget,self.imageItem,row=0,col=1)
        # self.plotSum = self.setupHistItem(self.viewer_GraphicsLayoutWidget,self.imageItem,row=0,col=1)
        self.updateGUI()
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
        self.showSum_checkBox.stateChanged.connect(self.updateGUI)
        self.showHist_checkBox.stateChanged.connect(self.updateGUI)

    def showHideWidget(self,items,show_bool = True):
        if show_bool:        
            [item.show() for item in items]
        else:
            [item.hide() for item in items]

    def updateGUI(self):
        self.showHideWidget([self.plot_2D],self.show2D_checkBox.isChecked())
        # self.showHideWidget([self.plot_2D],self.showSum_checkBox.isChecked())
        self.showHideWidget([self.histLUT_2D],self.showHist_checkBox.isChecked())

    def setupImageWidget(self,layout,title = '', row = None, col = None):
        plot = layout.addPlot(title=title,labels={'bottom': ('x axis title'), 'left': ('y axis title')},row = row, col = col)
        plot.ctrlMenu = None
        view = plot.getViewBox()
        img = pg.ImageItem()                
        img.setImage(np.eye(3),autoRange=True)
        plot.addItem(img)     
        return plot,view,img




    def setupHistItem(self,layout,image,row = None, col = None):
        hist = pg.HistogramLUTItem(gradientPosition="left")
        hist.gradient.setColorMap(pg.colormap.get('hot', source='matplotlib'))
        layout.addItem(hist,row = row, col = col)
        hist.setImageItem(image)   
        hist.autoHistogramRange()
        return hist

    def setupPlot(self,layout,row = None, col = None):
        plotItem = pg.PlotDataItem()    
        plot = layout.addPlot(row = row, col = col)
        plot.addItem(plotItem)
        return plot,plotItem
    
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



    # def showROIPanel(self,input):
    #     roi = pg.LinearRegionItem()
    #     self.signalInput_Plot.addItem(roi)        
    #     print('ok')
    # def setupContextMenu(self,menu):
    #     action = QAction('Add ROI',parent =menu)
    #     menu.addAction(action)
    #     menu.removeAction(menu.actions()[3])
    #     action.triggered.connect(self.showROIPanel)



def main():
    import sys
    app = QApplication([])
    tof = ViewerWidget()
    tof.show()
    app.exec()

if __name__=="__main__":
    main()




    