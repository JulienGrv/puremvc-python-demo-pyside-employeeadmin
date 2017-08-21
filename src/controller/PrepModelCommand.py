# -*- coding: utf-8 -*-

from puremvc.patterns.command import SimpleCommand

from .. import model


class PrepModelCommand(SimpleCommand):
    """
    Prepare the Model.
    """

    def execute(self, notification):
        # Create User Proxy
        userProxy = model.UserProxy()

        # Populate it with dummy data
        userProxy.addItem(
            model.vo.UserVO('lstooge', 'Larry', 'Stooge', 'larry@stooges.com',
                            'ijk456', model.enum.DeptEnum.ACCT))
        userProxy.addItem(
            model.vo.UserVO('cstooge', 'Curly', 'Stooge', 'curly@stooges.com',
                            'xyz987', model.enum.DeptEnum.SALES))
        userProxy.addItem(
            model.vo.UserVO('mstooge', 'Moe', 'Stooge', 'moe@stooges.com',
                            'abc123', model.enum.DeptEnum.PLANT))

        # Register it
        self.facade.registerProxy(userProxy)

        # Create Role Proxy
        roleProxy = model.RoleProxy()

        # Populate it with dummy data
        roleProxy.addItem(
            model.vo.RoleVO('lstooge', [
                model.enum.RoleEnum.PAYROLL, model.enum.RoleEnum.EMP_BENEFITS
            ]))
        roleProxy.addItem(
            model.vo.RoleVO('cstooge', [
                model.enum.RoleEnum.ACCT_PAY, model.enum.RoleEnum.ACCT_RCV,
                model.enum.RoleEnum.GEN_LEDGER
            ]))
        roleProxy.addItem(
            model.vo.RoleVO('mstooge', [
                model.enum.RoleEnum.INVENTORY, model.enum.RoleEnum.PRODUCTION,
                model.enum.RoleEnum.SALES, model.enum.RoleEnum.SHIPPING
            ]))

        # Register it
        self.facade.registerProxy(roleProxy)
