# -*- coding: utf-8 -*-

from puremvc.patterns.mediator import Mediator


class MainWindowMediator(Mediator):
    """
    """

    NAME = 'MainWindowMediator'

    def __init__(self, mediatorName=None, viewComponent=None):
        super(MainWindowMediator, self).__init__(mediatorName, viewComponent)
