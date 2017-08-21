# -*- coding: utf-8 -*-

import sys

from . import ApplicationFacade


def main():
    app = ApplicationFacade.getInstance()
    app.startup(sys.argv)


if __name__ == '__main__':
    sys.exit(main())
