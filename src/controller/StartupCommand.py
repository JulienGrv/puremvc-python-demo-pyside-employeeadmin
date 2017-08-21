# -*- coding: utf-8 -*-

from puremvc.patterns.command import MacroCommand

from .PrepModelCommand import PrepModelCommand
from .PrepViewCommand import PrepViewCommand


class StartupCommand(MacroCommand):

    def initializeMacroCommand(self):
        """
        Add the Subcommands to startup the PureMVC apparatus.

        Generally, it is best to prep the Model (mostly registering proxies)
        followed by preparation of the View (mostly registering mediators).
        """
        self.addSubCommand(PrepModelCommand)
        self.addSubCommand(PrepViewCommand)
