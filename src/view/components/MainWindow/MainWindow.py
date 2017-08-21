# -*- coding: utf-8 -*-

from PySide import QtGui
from .Ui_MainWindow import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        layout = QtGui.QGridLayout(self.centralWidget())
        self.centralWidget().setLayout(layout)
