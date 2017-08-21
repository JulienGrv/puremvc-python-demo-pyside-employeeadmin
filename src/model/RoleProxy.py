# -*- coding: utf-8 -*-

from puremvc.patterns.proxy import Proxy

from .. import ApplicationFacade


class RoleProxy(Proxy):

    NAME = 'RoleProxy'

    def __init__(self, proxyName=None, data=[]):
        super(RoleProxy, self).__init__(proxyName, data)
        self.data = data

    def addItem(self, role):
        self.data.append(role)

    def deleteItem(self, user):
        for role in self.data:
            if role.username == user.username:
                self.data.remove(role)
                break

    def doesUserHaveRole(self, user, role):
        return role in self.getUserRoles(user.username)

    def addRoleToUser(self, user, role):
        result = False
        if not self.doesUserHaveRole(user, role):
            userRoles = self.getUserRoles(user.username)
            userRoles.append(role)
            result = True
        self.sendNotification(ApplicationFacade.ADD_ROLE_RESULT, result)

    def removeRoleFromUser(self, user, role):
        if self.doesUserHaveRole(user, role):
            userRoles = self.getUserRoles(user.username)
            userRoles.remove(role)

    def getUserRoles(self, username):
        userRoles = None
        for userRoles in self.data:
            if userRoles.username == username:
                break
        return userRoles.roles
