# -*- coding: utf-8 -*-

from puremvc.patterns.proxy import Proxy


class UserProxy(Proxy):

    NAME = 'UserProxy'

    def __init__(self, proxyName=None, data=[]):
        super(UserProxy, self).__init__(proxyName, data)
        self.data = data

    def addItem(self, user):
        self.data.append(user)

    def updateItem(self, user):
        for usr in self.data:
            if usr.username == user.username:
                usr = user

    def deleteItem(self, user):
        self.data.remove(user)
