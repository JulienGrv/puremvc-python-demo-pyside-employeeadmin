# -*- coding: utf-8 -*-

from puremvc.patterns.facade import Facade


class ApplicationFacade(Facade):

    # Notification name constants
    # Commands
    ADD_ROLE_RESULT = 'addRoleResult'
    DELETE_USER = 'deleteUser'
    STARTUP = 'startup'
    # Mediators
    ADD_ROLE = 'addRole'
    ADD_ROLE_RESULT = 'addRoleResult'
    CANCEL_SELECTED = 'cancelSelected'
    NEW_USER = 'newUser'
    POPULATE_USER = 'populateUsers'
    USER_ADDED = 'userAdded'
    USER_DELETED = 'userDeleted'
    USER_SELECTED = 'userSelected'
    USER_UPDATED = 'userUpdated'

    @staticmethod
    def getInstance():
        return ApplicationFacade()

    def startup(self, args):
        from . import controller
        self.registerCommand(self.STARTUP, controller.StartupCommand)
        self.registerCommand(self.DELETE_USER, controller.DeleteUserCommand)
        self.registerCommand(self.ADD_ROLE_RESULT,
                             controller.AddRoleResultCommand)
        self.sendNotification(self.STARTUP, args)
