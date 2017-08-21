# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui

from .Ui_UserTableWidget import Ui_UserTableWidget


class UserTableWidget(QtGui.QWidget):

    NEW = ('newPushButton', 'clicked()')
    DELETE = ('deletePushButton', 'clicked()')
    SELECT = ('tableView', 'selectionChanged()')

    @property
    def selectedUser(self):
        selectionModel = self.ui.tableView.selectionModel()
        indexes = selectionModel.selectedRows()
        if len(indexes) == 1:
            index = indexes[0]
            username = self.userTableModel.data(index)
            return username
        return None

    def __init__(self, parent=None):
        super(UserTableWidget, self).__init__(parent)

        self.ui = Ui_UserTableWidget()
        self.ui.setupUi(self)

        self.userTableModel = UserTableModel(self)
        self.ui.tableView.setModel(self.userTableModel)
        self.ui.tableView.setEditTriggers(
            QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.tableView.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(
            QtGui.QAbstractItemView.SingleSelection)
        self.ui.tableView.verticalHeader().hide()
        self.ui.tableView.horizontalHeader().resizeSections(
            QtGui.QHeaderView.ResizeToContents)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.countLabel.setText(str(self.userTableModel.rowCount()))

    def addEventListener(self, event, callback):
        if event == self.NEW:
            self.ui.newPushButton.clicked.connect(callback)
        elif event == self.DELETE:
            self.ui.deletePushButton.clicked.connect(callback)
        elif event == self.SELECT:
            selectionModel = self.ui.tableView.selectionModel()
            selectionModel.selectionChanged.connect(callback)

    def addItem(self, user):
        rowCount = self.userTableModel.rowCount()
        self.userTableModel.insertRow(rowCount)
        index = self.userTableModel.index(rowCount, 0, QtCore.QModelIndex())
        self.userTableModel.setData(index, user.username)
        index = self.userTableModel.index(rowCount, 1, QtCore.QModelIndex())
        self.userTableModel.setData(index, user.firstname)
        index = self.userTableModel.index(rowCount, 2, QtCore.QModelIndex())
        self.userTableModel.setData(index, user.lastname)
        index = self.userTableModel.index(rowCount, 3, QtCore.QModelIndex())
        self.userTableModel.setData(index, user.email)
        index = self.userTableModel.index(rowCount, 4, QtCore.QModelIndex())
        self.userTableModel.setData(index, user.department)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.countLabel.setText(str(self.userTableModel.rowCount()))


class UserTableModel(QtCore.QAbstractTableModel):

    HEADERS = ['Username', 'First Name', 'Last Name', 'Email', 'Department']

    def __init__(self, parent=None):
        self._users = []
        super(UserTableModel, self).__init__(parent)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._users)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.HEADERS)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        if not 0 <= index.row() < len(self._users):
            return None
        if role == QtCore.Qt.DisplayRole:
            user = self._users[index.row()]
            return user[self.HEADERS[index.column()]]
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.HEADERS[section]
        return None

    def insertRows(self, row, count, parent=QtCore.QModelIndex()):
        self.beginInsertRows(QtCore.QModelIndex(), row, count)
        for row in range(count):
            self._users.insert(row + count + 1,
                               {header: None
                                for header in self.HEADERS})
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QtCore.QModelIndex):
        self.beginRemoveRows(QtCore.QModelIndex(), index, count)
        del self._users[row:row + count]
        self.endRemoveRows()
        return True

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role != QtCore.Qt.EditRole:
            return False
        if index.isValid() and 0 <= index.row() < len(self._users):
            user = self._users[index.row()]
            user[self.HEADERS[index.column()]] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        """ Set the item flags at the given index. Seems like we're 
            implementing this function just to see how it's done, as we 
            manually adjust each tableView to have NoEditTriggers.
        """
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemFlags(
            QtCore.QAbstractTableModel.flags(self, index) |
            QtCore.Qt.ItemIsEditable)
