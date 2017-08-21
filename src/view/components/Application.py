# -*- coding: utf-8 -*-

from PySide import QtGui

from .MainWindow import MainWindow


class Application(QtGui.QApplication):

    def __init__(self, args):
        super(Application, self).__init__(args)
        self.windows = {}

    def addWindow(self, window, show=True):
        self.windows[window.objectName()] = window
        if show:
            window.show()
