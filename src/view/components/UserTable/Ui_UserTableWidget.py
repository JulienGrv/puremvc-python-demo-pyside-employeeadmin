# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui/UserTableWidget.ui'
#
# Created: Wed Aug 16 03:27:48 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_UserTableWidget(object):

    def setupUi(self, UserTableWidget):
        UserTableWidget.setObjectName("UserTableWidget")
        self.gridLayout = QtGui.QGridLayout(UserTableWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.deletePushButton = QtGui.QPushButton(UserTableWidget)
        self.deletePushButton.setObjectName("deletePushButton")
        self.horizontalLayout_2.addWidget(self.deletePushButton)
        self.newPushButton = QtGui.QPushButton(UserTableWidget)
        self.newPushButton.setObjectName("newPushButton")
        self.horizontalLayout_2.addWidget(self.newPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.tableView = QtGui.QTableView(UserTableWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(UserTableWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth(
        ))
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.countLabel = QtGui.QLabel(UserTableWidget)
        self.countLabel.setObjectName("countLabel")
        self.horizontalLayout.addWidget(self.countLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.retranslateUi(UserTableWidget)
        QtCore.QMetaObject.connectSlotsByName(UserTableWidget)

    def retranslateUi(self, UserTableWidget):
        UserTableWidget.setWindowTitle(
            QtGui.QApplication.translate("UserTableWidget", "User Table", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.deletePushButton.setText(
            QtGui.QApplication.translate("UserTableWidget", "Delete", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.newPushButton.setText(
            QtGui.QApplication.translate("UserTableWidget", "New", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("UserTableWidget", "Users", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.countLabel.setText(
            QtGui.QApplication.translate("UserTableWidget", "count", None,
                                         QtGui.QApplication.UnicodeUTF8))
