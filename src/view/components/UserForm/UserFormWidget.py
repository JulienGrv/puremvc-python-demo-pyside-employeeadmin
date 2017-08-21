# -*- coding: utf-8 -*-

from PySide import QtGui
from .Ui_UserFormWidget import Ui_UserFormWidget


class UserFormWidget(QtGui.QWidget):

    # Edit modes
    MODE_ADD = 'modeAdd'
    MODE_EDIT = 'modeEdit'

    # Event
    UPDATE_PROFILE = ('updateProfilePushButton', 'clicked()')
    CANCEL = ('cancelPushButton', 'clicked()')

    @property
    def user(self):
        self._user.firstname = self.ui.firstNameLineEdit.text()
        self._user.lastname = self.ui.lastNameLineEdit.text()
        self._user.email = self.ui.emailLineEdit.text()
        self._user.username = self.ui.usernameLineEdit.text()
        self._user.password = self.ui.passwordLineEdit.text()
        self._user.department = self.ui.departmentComboBox.currentText()
        return self._user

    @user.setter
    def user(self, user):
        self._user = user
        if user:
            self.ui.label.setText(user.username)
            self.ui.firstNameLineEdit.setText(user.firstname)
            self.ui.lastNameLineEdit.setText(user.lastname)
            self.ui.emailLineEdit.setText(user.email)
            self.ui.usernameLineEdit.setText(user.username)
            self.ui.passwordLineEdit.setText(user.password)
            # self.ui.departmentComboBox.setCurrentText(user.department)
        else:
            self.ui.label.setText(None)
            self.ui.firstNameLineEdit.setText(None)
            self.ui.lastNameLineEdit.setText(None)
            self.ui.emailLineEdit.setText(None)
            self.ui.usernameLineEdit.setText(None)
            self.ui.passwordLineEdit.setText(None)
            self.ui.departmentComboBox.setCurrentIndex(-1)

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        if mode in [self.MODE_ADD, self.MODE_EDIT]:
            self._mode = mode
            self.setEnabled(True)
            if mode == self.MODE_EDIT:
                self.ui.usernameLineEdit.setEnabled(False)
            self.ui.firstNameLineEdit.setFocus()
        self._mode = None

    @property
    def departments(self):
        return self._departments

    @departments.setter
    def department(self, departments):
        if departments and len(departments) > 0:
            self._departments = departments
            for department in departments:
                self.ui.departmentComboBox.addItem(department)
        else:
            self.ui.departmentComboBox.clear()
            return None

    def __init__(self, parent=None):
        super(UserFormWidget, self).__init__(parent)

        self.ui = Ui_UserFormWidget()
        self.ui.setupUi(self)
        self.setEnabled(False)

        self._user = None
        self._mode = None
        self._departments = None

    def addEventListener(self, event, callback):
        if event == self.UPDATE_PROFILE:
            self.ui.updateProfilePushButton.clicked.connect(callback)
        elif event == self.CANCEL:
            self.ui.cancelPushButton.clicked.connect(callback)

    def reset(self):
        self.ui.usernameLabel.setText('username')
        self.ui.firstNameLineEdit.setText(None)
        self.ui.lastNameLineEdit.setText(None)
        self.ui.emailLineEdit.setText(None)
        self.ui.usernameLineEdit.setText(None)
        self.ui.passwordLineEdit.setText(None)
        self.ui.confirmPasswordLineEdit.setText(None)
        self.ui.departmentComboBox.setCurrentIndex(-1)
