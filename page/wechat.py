from appium.webdriver.common.appiumby import AppiumBy
from common.element import Element
from common.page import Page


class WeChatPage(Page):
    app = Element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="微信"]')

    def start_page(self):
        WeChatPage.app.click()
