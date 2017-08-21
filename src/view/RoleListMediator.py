# -*- coding: utf-8 -*-

from puremvc.patterns.mediator import Mediator

from .. import ApplicationFacade, model


class RoleListMediator(Mediator):
    """
    Role list component Mediator.
    """

    NAME = 'RoleListMediator'

    def __init__(self, mediatorName=None, viewComponent=None):
        super(RoleListMediator, self).__init__(mediatorName, viewComponent)

    def listNotificationInterests(self):
        return [
            ApplicationFacade.NEW_USER, ApplicationFacade.USER_ADDED,
            ApplicationFacade.USER_UPDATED, ApplicationFacade.USER_DELETED,
            ApplicationFacade.CANCEL_SELECTED, ApplicationFacade.USER_SELECTED,
            ApplicationFacade.ADD_ROLE_RESULT
        ]

    def handleNotification(self, notification):
        name = notification.getName()
        roleList = self.viewComponent
        if name == ApplicationFacade.NEW_USER:
            self.clearForm()
        elif name == ApplicationFacade.USER_ADDED:
            roleList.user = notification.getBody()
            role = model.vo.RoleVO(roleList.user.username)
            self.roleProxy.addIem(role)
            self.clearForm()
            roleList.setEnabled(False)
        elif name == ApplicationFacade.USER_UPDATED:
            self.clearForm()
            roleList.setEnabled(False)
        elif name == ApplicationFacade.USER_DELETED:
            self.clearForm()
            roleList.setEnabled(False)
        elif name == ApplicationFacade.CANCEL_SELECTED:
            self.clearForm()
            roleList.setEnabled(False)
        elif name == ApplicationFacade.USER_SELECTED:
            roleList.user = notification.getBody()
            roleList.userRoles = self.roleProxy.getUserRoles(
                roleList.user.username)
            roleList.reset()
            roleList.setEnabled(True)
        elif name == ApplicationFacade.ADD_ROLE_RESULT:
            roleList.userRoles = self.roleProxy.getUserRoles(
                roleList.user.username)
            roleList.reset()

    def clearForm(self):
        roleList = self.viewComponent
        roleList.user = None
        roleList.userRoles = None
        roleList.reset()

    def onRegister(self):
        self.viewComponent.roles = model.enum.RoleEnum()
        self.roleProxy = self.facade.retrieveProxy(model.RoleProxy.NAME)
        self.viewComponent.addEventListener(self.viewComponent.ADD,
                                            self.onAddRole)
        self.viewComponent.addEventListener(self.viewComponent.REMOVE,
                                            self.onRemoveRole)

    def onAddRole(self):
        self.roleProxy.addRoleToUser(self.viewComponent.user,
                                     self.viewComponent.selectedRole)

    def onRemoveRole(self):
        self.roleProxy.removeRoleFromUser(self.viewComponent.user,
                                          self.viewComponent.selectedRole)
