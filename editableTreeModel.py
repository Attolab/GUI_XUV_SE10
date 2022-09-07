#!/usr/bin/env python

############################################################################
##
## Copyright (C) 2005-2005 Trolltech AS. All rights reserved.
##
## This file is part of the example classes of the Qt Toolkit.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http://www.trolltech.com/products/qt/opensource.html
##
## If you are unsure which license is appropriate for your use, please
## review the following information:
## http://www.trolltech.com/products/qt/licensing.html or contact the
## sales department at sales@trolltech.com.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
############################################################################

from PySide6 import QtCore, QtGui, QtWidgets
import numpy as np 

class TreeItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []
    def getDepth(self,):       
        if self.parentItem:            
            return 1 + self.parentItem.getDepth()
        else:
            return 0

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def childNumber(self):
        if self.parentItem != None:
            return self.parentItem.childItems.index(self)
        return 0

    def columnCount(self):
        return len(self.itemData)

    def data(self, column):
        return self.itemData[column]

    def insertChildren(self, position, count, columns):
        if position < 0 or position > len(self.childItems):
            return False

        for row in range(count):
            data = [None for v in range(columns)]
            item = TreeItem(data, self)
            self.childItems.insert(position, item)

        return True

    def insertColumns(self, position, columns):
        if position < 0 or position > len(self.itemData):
            return False

        for column in range(columns):
            self.itemData.insert(position, None)

        for child in self.childItems:
            child.insertColumns(position, columns)

        return True

    def parent(self):
        return self.parentItem

    def removeChildren(self, position, count):
        if position < 0 or position + count > len(self.childItems):
            return False

        for row in range(count):
            self.childItems.pop(position)

        return True

    def removeColumns(self, position, columns):
        if position < 0 or position + columns > len(self.itemData):
            return False

        for column in range(columns):
            self.itemData.pop(position)

        for child in self.childItems:
            child.removeColumns(position, columns)

        return True

    def setData(self, column, value):
        if column < 0 or column >= len(self.itemData):
            return False

        self.itemData[column] = value

        return True


class TreeModel(QtCore.QAbstractItemModel):
    nodeKeyChanged_signal = QtCore.Signal(object)
    nodeKeyRemoved_signal = QtCore.Signal(object)
    def __init__(self, headers, data, parent=None):
        super(TreeModel, self).__init__(parent)

        rootData = [header for header in headers]
        
        self.rootItem = TreeItem(['' for header in headers])
        self.rootHeaderItem = TreeItem(rootData,self.rootItem)
        self.nodes = {}
        self.buildTree(data, self.rootItem, hideRoot=True)
        self.connectSignal()
    def connectSignal(self):
        self.dataChanged.connect(self.dataChanged_slot)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return self.rootItem.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None

        if role != QtCore.Qt.DisplayRole and role != QtCore.Qt.EditRole:
            return None

        item = self.getItem(index)
        return item.data(index.column())

    def flags(self, index):
        if not index.isValid():
            return 0

        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def getItem(self, index):
        if index.isValid():
            item = index.internalPointer()
            if item:
                return item

        return self.rootItem

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootHeaderItem.data(section)

        return None

    def index(self, row, column, parent=QtCore.QModelIndex()):
        if parent.isValid() and parent.column() != 0:
            return QtCore.QModelIndex()

        parentItem = self.getItem(parent)
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def insertColumns(self, position, columns, parent=QtCore.QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)
        success = self.rootItem.insertColumns(position, columns)
        self.endInsertColumns()

        return success

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        parentItem = self.getItem(parent)
        self.beginInsertRows(parent, position, position + rows - 1)
        success = parentItem.insertChildren(position, rows,
                self.rootItem.columnCount())
        self.endInsertRows()

        return success

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = self.getItem(index)
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QtCore.QModelIndex()

        return self.createIndex(parentItem.childNumber(), 0, parentItem)

    def removeColumns(self, position, columns, parent=QtCore.QModelIndex()):
        self.beginRemoveColumns(parent, position, position + columns - 1)
        success = self.rootItem.removeColumns(position, columns)
        self.endRemoveColumns()

        if self.rootItem.columnCount() == 0:
            self.removeRows(0, self.rowCount())

        return success

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        parentItem = self.getItem(parent)

        self.beginRemoveRows(parent, position, position + rows - 1)
        success = parentItem.removeChildren(position, rows)
        self.endRemoveRows()

        return success

    def rowCount(self, parent=QtCore.QModelIndex()):
        parentItem = self.getItem(parent)

        return parentItem.childCount()

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role != QtCore.Qt.EditRole:
            return False

        item = self.getItem(index)
        result = item.setData(index.column(), value)

        if result:
            self.dataChanged.emit(index, index)

        return result

    def setHeaderData(self, section, orientation, value, role=QtCore.Qt.EditRole):
        if role != QtCore.Qt.EditRole or orientation != QtCore.Qt.Horizontal:
            return False

        result = self.rootItem.setData(section, value)
        if result:
            self.headerDataChanged.emit(orientation, section, section)

        return result
          

    def buildTree(self, data, parent, name='', hideRoot=False, path=()):        
        typeStr, desc, childs = self.parse(data)
        if hideRoot:
            node = parent
        else:
            if path not in self.nodes:
                parent.insertChildren(parent.childCount(), 1, parent.columnCount()) #New entry
                typeStr, desc, childs = self.parse(data)
                node = parent.child(parent.childCount() - 1)
                self.nodes[path] = node
                node.setData(0, name)
                node.setData(1, typeStr)
                node.setData(2, desc)    
            else:
                node = self.nodes[path]
        # recurse to children
        for key, data in childs.items():
            self.buildTree(data, node, str(key), path=path+(key,))

    def parse(self, data):
            """
            Given any python object, return:
            * type
            * a short string representation
            * a dict of sub-objects to be parsed
            * optional widget to display as sub-node
            """
            # defaults for all objects
            typeStr = type(data).__name__
            desc = ""
            childs = {}            
            # type-specific changes
            if isinstance(data, dict):
                desc = "length=%d" % len(data)
                childs = data              
            elif isinstance(data, (list, tuple)):
                desc = "length=%d" % len(data)
                childs = dict(enumerate(data))
            elif isinstance(data, np.ndarray):
                desc = "shape=%s dtype=%s" % (data.shape, data.dtype)
            else:
                desc = str(data)            
            return typeStr, desc, childs


    def findUpperparent(self,item):
        if item.parentItem != self.rootItem:
            parent = self.findUpperparent(item.parentItem) 
        else:
            parent = item        
        return parent

    def dataChanged_slot(self,index):
        self.updateNodesKey(self.getItem(index))    


    def getAdress(self,item,path = ()):
            if item.parentItem != self.rootItem:
                path += self.getAdress(item.parentItem,)
            path += (item.data(0),)
            return path
            
    def updateNodesKey(self,item):
        for k,v in self.nodes.items():
            if v == item:
                break
        [self.updateNodesKey(childItem) for childItem in item.childItems] # Apply to all children
        new_key = self.getAdress(item,())
        if not item.childItems: #┘Only send signal to update data
            self.nodeKeyChanged_signal.emit((k,new_key))
        self.nodes[new_key] = self.nodes.pop(k)

    def removeNodesEntry(self,item):
        for k,v in self.nodes.items():
            if v == item:
                break
        [self.removeNodesEntry(childItem) for childItem in item.childItems] # Apply to all children
        self.nodeKeyRemoved_signal.emit(k)
        self.nodes.pop(k)

    def clear(self):
        self.beginResetModel()
        self.removeRows(0,self.rowCount())
        self.nodes = {}
        self.endResetModel()

class NoEditDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        QtWidgets.QStyledItemDelegate.__init__(self, parent)
    def createEditor(self,parent,option,index):
        if index.column() == 0:            
            return QtWidgets.QStyledItemDelegate.createEditor(self, parent, option,index)   
                                                  
    # def setEditorData(self, editor,index):
    #     value = index.model().data(index, QtCore.Qt.EditRole)
    #     line_edit = QtWidgets.QLineEdit(editor)
    #     line_edit.setText(value)

    # def setModelData(self, editor, model,index):
    #     line_edit = QtWidgets.QLineEdit(editor)
    #     value = line_edit.text()
    #     model.setData(index, value, QtCore.Qt.EditRole)        
    # def updateEditorGeometry(self, editor,option,index):
    #     editor.setGeometry(option.rect)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
