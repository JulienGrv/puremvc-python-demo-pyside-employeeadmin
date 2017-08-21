# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/ui/RoleListWidget.ui'
#
# Created: Wed Aug 16 03:25:30 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_RoleListWidget(object):

    def setupUi(self, RoleListWidget):
        RoleListWidget.setObjectName("RoleListWidget")
        self.gridLayout = QtGui.QGridLayout(RoleListWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.roleComboBox = QtGui.QComboBox(RoleListWidget)
        self.roleComboBox.setObjectName("roleComboBox")
        self.horizontalLayout_2.addWidget(self.roleComboBox)
        self.addPushButton = QtGui.QPushButton(RoleListWidget)
        self.addPushButton.setObjectName("addPushButton")
        self.horizontalLayout_2.addWidget(self.addPushButton)
        self.removePushButton = QtGui.QPushButton(RoleListWidget)
        self.removePushButton.setObjectName("removePushButton")
        self.horizontalLayout_2.addWidget(self.removePushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(RoleListWidget)
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
        self.fullnameLabel = QtGui.QLabel(RoleListWidget)
        self.fullnameLabel.setObjectName("fullnameLabel")
        self.horizontalLayout.addWidget(self.fullnameLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.listView = QtGui.QListView(RoleListWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)

        self.retranslateUi(RoleListWidget)
        QtCore.QMetaObject.connectSlotsByName(RoleListWidget)

    def retranslateUi(self, RoleListWidget):
        RoleListWidget.setWindowTitle(
            QtGui.QApplication.translate("RoleListWidget", "Role List", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.addPushButton.setText(
            QtGui.QApplication.translate("RoleListWidget", "Add", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.removePushButton.setText(
            QtGui.QApplication.translate("RoleListWidget", "Remove", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("RoleListWidget", "User Roles", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.fullnameLabel.setText(
            QtGui.QApplication.translate("RoleListWidget", "fullname", None,
                                         QtGui.QApplication.UnicodeUTF8))
