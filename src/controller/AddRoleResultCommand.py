# -*- coding: utf-8 -*-

from puremvc.patterns.command import SimpleCommand

from .. import ApplicationFacade


class AddRoleResultCommand(SimpleCommand):

    def execute(self, notification):
        result = notification.getBody()
        if not result:
            self.facade.sendNotification(ApplicationFacade.SHOW_DIALOG,
                                         'Role already exists for this user!')
