# -*- coding: utf-8 -*-


class RoleEnum(list):
    NONE_SELECTED = '--None Selected--'
    ADMIN = 'Administrator'
    ACCT_PAY = 'Accounts Payable'
    ACCT_RCV = 'Accounts Receivable'
    EMP_BENEFITS = 'Employee Benefits'
    GEN_LEDGER = 'General Ledger'
    PAYROLL = 'Payroll'
    INVENTORY = 'Inventory'
    PRODUCTION = 'Production'
    QUALITY_CTL = 'Quality Control'
    SALES = 'Sales'
    ORDERS = 'Orders'
    CUSTOMERS = 'Customers'
    SHIPPING = 'Shipping'
    RETURNS = 'Returns'

    def __init__(self):
        enum = [
            self.NONE_SELECTED, self.ADMIN, self.ACCT_PAY, self.ACCT_RCV,
            self.EMP_BENEFITS, self.GEN_LEDGER, self.PAYROLL, self.INVENTORY,
            self.PRODUCTION, self.QUALITY_CTL, self.SALES, self.ORDERS,
            self.CUSTOMERS, self.SHIPPING, self.RETURNS
        ]
        super(RoleEnum, self).__init__(enum)
