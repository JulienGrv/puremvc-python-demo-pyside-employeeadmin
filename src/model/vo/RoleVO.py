# -*- coding: utf-8 -*-


class RoleVO(object):

    def __init__(self, username='', roles=[]):
        self.username = username
        self.roles = roles

    def __str__(self):
        return 'username: {}, roles: {}'.format(self.username, self.roles)
