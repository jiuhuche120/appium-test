from common.driver import Driver


class Element(object):
    def __init__(self, by, value):
        self.by = by
        self.value = value

    def click(self):
        Driver.driver.find_element(self.by, self.value).click()

    def send_keys(self, keys):
        Driver.driver.find_element(self.by, self.value).send_keys(keys)


