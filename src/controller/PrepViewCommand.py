# -*- coding: utf-8 -*-

from puremvc.patterns.command import SimpleCommand

from .. import view


class PrepViewCommand(SimpleCommand):
    """
    Prepare the View.

    Get the view Components for the Mediators from the app,
    a reference to which was passed on the original startup notification.
    """

    def execute(self, notification):
        argv = notification.getBody()
        app = view.components.Application(argv)
        # mainWindow = app.activeWindow()
        mainWindow = view.components.MainWindow()
        app.addWindow(mainWindow)
        centralWidget = mainWindow.centralWidget()
        userTable = view.components.UserTableWidget(centralWidget)
        userForm = view.components.UserFormWidget(centralWidget)
        roleList = view.components.RoleListWidget(centralWidget)
        gridLayout = mainWindow.centralWidget().layout()
        gridLayout.addWidget(userTable, 0, 0, 1, 2)
        gridLayout.addWidget(userForm, 1, 0, 1, 1)
        gridLayout.addWidget(roleList, 1, 1, 1, 1)
        self.facade.registerMediator(
            view.MainWindowMediator(viewComponent=mainWindow))
        self.facade.registerMediator(
            view.UserTableMediator(viewComponent=userTable))
        self.facade.registerMediator(
            view.UserFormMediator(viewComponent=userForm))
        self.facade.registerMediator(
            view.RoleListMediator(viewComponent=roleList))
        app.exec_()

        # # View components are initialized using the application main window
        # # central wiget
        # userForm = UserFormWidget(mainWindow.centralWidget())
        # userTable = UserTableWidget(mainWindow.centralWidget())
        # roleList = RoleListWidget(mainWindow.centralWidget())

        # # Register mediators
        # # self.facade.registerMediator(
        # #     UserFormMediator(MediatorNames.USER_FORM_MEDIATOR, userForm))
        # # self.facade.registerMediator(
        # #     UserTableMediator(MediatorNames.USER_TABLE_MEDIATOR, userTable))
        # self.facade.registerMediator(
        #     RoleListMediator(MediatorNames.ROLE_LIST_MEDIATOR, roleList))
