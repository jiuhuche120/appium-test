import configparser
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options


class Driver(object):
    driver = None

    def __init__(self):
        root_dir = os.path.dirname(os.path.dirname(__file__))
        config_dir = os.path.join(root_dir, 'config', 'config.ini')
        cf = configparser.ConfigParser()
        cf.read(config_dir, encoding="utf-8")
        self.config = cf
        self.host = self.config.get("config", "host")
        self.port = self.config.get("config", "port")
        options = UiAutomator2Options()
        options.platform_name = self.config.get("config", "platform_name")
        options.platformVersion = self.config.get("config", "platformVersion")
        self.options = options
        Driver.driver = webdriver.Remote(
            command_executor='http://' + self.host + ':' + self.port + '/wd/hub',
            options=self.options
        )
