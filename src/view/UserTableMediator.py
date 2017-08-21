# -*- coding: utf-8 -*-

from puremvc.patterns.mediator import Mediator

from .. import ApplicationFacade, model


class UserTableMediator(Mediator):
    """
    """

    NAME = 'UserTableMediator'

    def __init__(self, mediatorName=None, viewComponent=None):
        super(UserTableMediator, self).__init__(mediatorName, viewComponent)

    def listNotificationInterests(self):
        return [
            ApplicationFacade.CANCEL_SELECTED, ApplicationFacade.USER_UPDATED
        ]

    def handleNotification(self, notification):
        name = notification.getName()
        if name == ApplicationFacade.CANCEL_SELECTED:
            self.viewComponent

    def onRegister(self):
        self.userProxy = self.facade.retrieveProxy(model.UserProxy.NAME)
        for user in self.userProxy.data:
            self.viewComponent.addItem(user)
        self.viewComponent.addEventListener(self.viewComponent.NEW, self.onNew)
        self.viewComponent.addEventListener(self.viewComponent.DELETE,
                                            self.onDelete)
        self.viewComponent.addEventListener(self.viewComponent.SELECT,
                                            self.onSelect)

    def onNew(self):
        self.sendNotification(ApplicationFacade.NEW_USER, model.vo.UserVO())

    def onDelete(self):
        username = self.viewComponent.selectedUser
        for user in self.userProxy.data:
            if user.username == username:
                break
        self.sendNotification(ApplicationFacade.DELETE_USER, user)

    def onSelect(self):
        username = self.viewComponent.selectedUser
        for user in self.userProxy.data:
            if user.username == username:
                break
        self.sendNotification(ApplicationFacade.USER_SELECTED, user)
