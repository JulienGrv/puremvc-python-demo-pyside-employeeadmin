# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from .Ui_RoleListWidget import Ui_RoleListWidget


class RoleListWidget(QtGui.QWidget):

    ADD = ('addPushButton', 'clicked()')
    REMOVE = ('removePushButton', 'clicked()')

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        if user:
            self._user = user
            self.ui.fullnameLabel.setText(user.givenName())
        else:
            self._user = None
            self.ui.fullnameLabel.setText(None)

    @property
    def userRoles(self):
        return self.roleListModel.data

    @userRoles.setter
    def userRoles(self, roles):
        rowCount = self.roleListModel.rowCount()
        self.roleListModel.removeRows(0, rowCount)
        if roles:
            for role in roles:
                rowCount = self.roleListModel.rowCount()
                self.roleListModel.insertRow(rowCount)
                index = self.roleListModel.index(rowCount, 0,
                                                 QtCore.QModelIndex())
                self.roleListModel.setData(index, role)

    @property
    def roles(self):
        return self._roles

    @roles.setter
    def roles(self, roles):
        if roles and len(roles) > 0:
            self._roles = roles
            for role in roles:
                self.ui.roleComboBox.addItem(role)
        else:
            self.ui.roleComboBox.clear()
            return None

    @property
    def selectedRole(self):
        return self.ui.roleComboBox.currentText()

    def __init__(self, parent=None):
        super(RoleListWidget, self).__init__(parent)

        self.ui = Ui_RoleListWidget()
        self.ui.setupUi(self)

        self.roleListModel = RoleListModel(self)
        self.ui.listView.setModel(self.roleListModel)
        self.ui.fullnameLabel.setText(None)
        self.setEnabled(False)

        self._user = None
        self._roles = None

    def addEventListener(self, event, callback):
        if event == self.ADD:
            self.ui.addPushButton.clicked.connect(callback)
        elif event == self.REMOVE:
            self.ui.removePushButton.clicked.connect(callback)


class RoleListModel(QtCore.QAbstractListModel):

    def __init__(self, parent=None):
        self._roles = []
        super(RoleListModel, self).__init__(parent)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._roles)

    def insertRows(self, row, count, parent=QtCore.QModelIndex()):
        self.beginInsertRows(QtCore.QModelIndex(), row, count)
        for row in range(count):
            self._roles.insert(row + count + 1, None)
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QtCore.QModelIndex):
        self.beginRemoveRows(QtCore.QModelIndex(), row, count)
        del self._roles[row:row + count]
        self.endRemoveRows()
        return True

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        if not 0 <= index.row() < len(self._roles):
            return None
        if role == QtCore.Qt.DisplayRole:
            return self._roles[index.row()]
        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role != QtCore.Qt.EditRole:
            return False
        if index.isValid() and 0 <= index.row() < len(self._roles):
            self._roles[index.row()] = value
            self.dataChanged.emit(index, index)
            return True
        return False
