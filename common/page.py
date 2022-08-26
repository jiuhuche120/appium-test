from common.driver import Driver


class Page(object):
    def __init__(self):
        if Driver.driver is None:
            Driver()

    def start_page(self):
        pass
