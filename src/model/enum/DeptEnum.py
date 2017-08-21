# -*- coding: utf-8 -*-


class DeptEnum(list):
    NONE_SELECTED = '--None Selected--'
    ACCT = 'Accounting'
    SALES = 'Sales'
    PLANT = 'Plant'
    SHIPPING = 'Shipping'
    QC = 'Quality Control'

    def __init__(self):
        enum = [
            self.NONE_SELECTED, self.ACCT, self.SALES, self.PLANT,
            self.SHIPPING, self.QC
        ]
        super(DeptEnum, self).__init__(enum)
