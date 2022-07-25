
"""
This example demonstrates the use of pyqtgraph's parametertree system. This provides
a simple way to generate user interfaces that control sets of parameters. The example
demonstrates a variety of different parameter types (int, float, list, etc.)
as well as some customized parameter types
"""

# `makeAllParamTypes` creates several parameters from a dictionary of config specs.
# This contains information about the options for each parameter so they can be directly
# inserted into the example parameter tree. To create your own parameters, simply follow
# the guidelines demonstrated by other parameters created here.

import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QAbstractItemView,QTreeWidgetItemIterator
import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter,ParameterTree
import numpy as np

# app = pg.mkQApp("Parameter Tree Example")
class CustomParameterTree(ParameterTree):
    removeItem_signal = Signal(int)
    itemSelected_signal = Signal(int,str)
    def __init__(self,parent=None):
        super(CustomParameterTree, self).__init__(parent)
        self.connectSignals()
        self.isUpdating = True
        # self.check_columnwidth()
    def connectSignals(self):
        # Table connection              
        self.itemSelectionChanged.connect(self.changeItemSelection)
        self.setHeaderHidden(True)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.itemSelectionChanged.connect(self.changeItemSelection)

    def get_selectedRows(self):
        return np.flip(np.unique([self.indexFromItem(item).row() for item in self.selectedItems() if item.param.type() == 'group']))

    def checkPlotSelection(self,item):
        return (item.param.name() != 'Plot List') & (item.param.type() == 'group')
    def changeItemSelection(self):
        if self.isUpdating:
            self.isUpdating = False
            row_sel = self.get_selectedRows()
            count = len(self.plot_list)                    
            for row in np.arange(count):
                if row in row_sel:
                    self.itemSelected_signal.emit(row,'selected')
                else:
                    self.itemSelected_signal.emit(row,'unselected')
            self.isUpdating = True
    def count_PlotTerm(self):
        count = 0
        iterator = QTreeWidgetItemIterator(self) # pass your treewidget as arg
        while iterator.value():
            # print(type(iterator.value()).__name__)
            if self.checkPlotSelection(iterator.value()):
                count +=1        
            iterator += 1
        return count

class PlotGroupParameters(pTypes.GroupParameter):
    valueChanging_signal = Signal(object,object)

    def __init__(self, **opts):
        opts['type'] = 'group'
        pTypes.GroupParameter.__init__(self, **opts)
        self.n = 0

    def addNew(self, parameters = None):
        pen_param = Parameter.create(name='pen_param',title='Pen parameters', type='pen',expanded = False)
        # shadowPen_param = Parameter.create(name='shadowpen_param',title='ShadowPen parameters', type='pen',expanded = False)
        if parameters:
            pen_param.updateFromPen(pen_param,parameters)
        # pen_param.sigValueChanged.connect(self.valueChanged)
        pen_param.sigValueChanging.connect(self.valueChanging)
        show_plot = Parameter.create(name= 'show_plot', title = 'Show',type= 'bool', value= True,expanded = False)
        # shadowPen_param = Parameter.create(name='shadowpen_param',title='ShadowPen parameters', type='pen',expanded = False)
        p = Parameter.create(name="Plot_%d" % (len(self.childs)+1), type='group', children=[show_plot,pen_param], removable=True, renamable=True,)   
        self.addChildren(
            [p,])
        print([[childs.name(),childs.value()] for childs in pen_param.childs])
    # def valueChanged(param, value):
    #     print("Value changed: %s %s" % (param, value))    
    def valueChanging(self,param, value):
        self.valueChanging_signal(param, value)
        self.n += 1
        print(self.n)
        if np.mod(self.n,2) == 0:
            print("Value changed: %s %s" % (param, value))    
            self.n = 0
        else:
            print("Value not changed: %s %s" % (param, value))    




## If anything changes in the tree, print a message
# def change(param, changes):
#     print("tree changes:")
#     for param, change, data in changes:
#         path = p.childPath(param)
#         if path is not None:
#             childName = '.'.join(path)
#         else:
#             childName = param.name()
#         print('  parameter: %s'% childName)
#         print('  change:    %s'% change)
#         print('  data:      %s'% str(data))
#         print('  ----------')    
# p.sigTreeStateChanged.connect(change)
        
# def save():
#     global state
#     state = p.saveState()

# def restore():
#     global state
#     add = p['Save/Restore functionality', 'Restore State', 'Add missing items']
#     rem = p['Save/Restore functionality', 'Restore State', 'Remove extra items']
#     p.restoreState(state, addChildren=add, removeChildren=rem)
# p.param('Save/Restore functionality', 'Save State').sigActivated.connect(save)
# p.param('Save/Restore functionality', 'Restore State').sigActivated.connect(restore)
# params = [
#     {'name': 'Save/Restore functionality', 'type': 'group', 'children': [
#         {'name': 'Save State', 'type': 'action'},
#         {'name': 'Restore State', 'type': 'action', 'children': [
#             {'name': 'Add missing items', 'type': 'bool', 'value': True},
#             {'name': 'Remove extra items', 'type': 'bool', 'value': True},
#         ]},
#     ]},    
#     PlotGroupParameters(name="plot_list",title="Plot List", tip='Click to add plot', children=[     
#     ]),
# ]

# ## Create tree of Parameter objects
# p = Parameter.create(name='params', type='group', children=params)
# t = ParameterTree()
# t.setParameters(p, showTop=False)
# t.setWindowTitle('Plot Parameter Tree')

# win = QtWidgets.QWidget()
# layout = QtWidgets.QGridLayout()
# win.setLayout(layout)
# layout.addWidget(t)
# win.show()

# ## test save/restore
# state = p.saveState()
# p.restoreState(state)
# compareState = p.saveState()
# assert pg.eq(compareState, state)

# if __name__ == '__main__':
#     pg.exec()
