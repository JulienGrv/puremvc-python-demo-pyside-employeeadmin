# -*- coding: utf-8 -*-

from puremvc.patterns.mediator import Mediator

from .. import ApplicationFacade, model


class UserFormMediator(Mediator):
    """
    """

    NAME = 'UserFormMediator'

    def __init__(self, mediatorName=None, viewComponent=None):
        super(UserFormMediator, self).__init__(mediatorName, viewComponent)

    def listNotificationInterests(self):
        return [
            ApplicationFacade.NEW_USER, ApplicationFacade.USER_DELETED,
            ApplicationFacade.USER_SELECTED
        ]

    def handleNotification(self, notification):
        name = notification.getName()
        if name == ApplicationFacade.NEW_USER:
            self.viewComponent.user = notification.getBody()
            self.viewComponent.mode = self.viewComponent.MODE_ADD
        elif name == ApplicationFacade.USER_DELETED:
            self.viewComponent.user = None
        elif name == ApplicationFacade.USER_SELECTED:
            self.viewComponent.user = notification.getBody()
            self.viewComponent.mode = self.viewComponent.MODE_EDIT

    def onRegister(self):
        self.viewComponent.departments = model.enum.DeptEnum()
        self.viewComponent.addEventListener(self.viewComponent.UPDATE_PROFILE,
                                            self.onUpdateProfile)
        self.viewComponent.addEventListener(self.viewComponent.CANCEL,
                                            self.onCancel)
        self.userProxy = self.facade.retrieveProxy(model.UserProxy.NAME)

    def onUpdateProfile(self):
        if self.viewComponent.mode == self.viewComponent.MODE_ADD:
            self.userProxy.addItem(self.viewComponent.user)
            self.sendNotification(ApplicationFacade.USER_ADDED,
                                  self.viewComponent.user)
        elif self.viewComponent.mode == self.viewComponent.MODE_EDIT:
            self.userProxy.updateItem(self.viewComponent.user)
            self.sendNotification(ApplicationFacade.USER_UPDATED,
                                  self.viewComponent.user)
        self.viewComponent.user = None

    def onCancel(self):
        self.sendNotification(ApplicationFacade.CANCEL_SELECTED)
        self.viewComponent.reset()
