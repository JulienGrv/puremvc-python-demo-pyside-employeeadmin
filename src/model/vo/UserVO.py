# -*- coding: utf-8 -*-

from ..enum import DeptEnum


class UserVO(object):

    def __init__(self,
                 username=None,
                 firstname=None,
                 lastname=None,
                 email=None,
                 password=None,
                 department=DeptEnum.NONE_SELECTED):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.department = department

    def isValid(self):
        return self.username and self.password and self.department != DeptEnum.NONE_SELECTED

    def givenName(self):
        return self.lastname + ', ' + self.firstname
