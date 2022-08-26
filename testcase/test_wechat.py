import allure

from page.wechat import WeChatPage


class TestWeChat:
    @allure.description('WeChat')
    def test_wechat(self):
        page = WeChatPage()
        page.start_page()
