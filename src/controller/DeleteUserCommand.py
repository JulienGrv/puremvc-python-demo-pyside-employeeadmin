# -*- coding: utf-8 -*-

from puremvc.patterns.command import SimpleCommand

from .. import ApplicationFacade, model


class DeleteUserCommand(SimpleCommand):

    def execute(self, notification):
        user = notification.getBody()
        userProxy = self.facade.retrieveProxy(model.UserProxy.NAME)
        roleProxy = self.facade.retrieveProxy(model.RoleProxy.NAME)
        userProxy.deleteItem(user)
        roleProxy.deleteItem(user)
        self.sendNotification(ApplicationFacade.USER_DELETED)
