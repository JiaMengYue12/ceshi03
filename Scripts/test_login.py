import os,sys

import pytest

sys.path.append(os.getcwd())

from Base.get_driver import getdriver
from Page.page_login import PageLogin


class TestLogin():
    # 初始化方法
    def setup_class(self):
        # 不加return，获取driver
        # self.driver = get_driver()
        # self.aike = PageLogin(self.driver)

        # 加return：
        self.aike=PageLogin(getdriver())

    # 结束方法
    def teardown_class(self):
        self.aike.driver.quit()


    # 测试方法
    def test_login01(self,username=18672090992,pwd=123456):
        self.aike.page_input_username(username)
        self.aike.page_input_password(pwd)
        self.aike.page_click_login_btn()

