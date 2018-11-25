# 登录爱客
import Page
from Base.base import Base


class PageLogin(Base):

    # 定位用户名
    def page_input_username(self,text):
        self.base_input(Page.loc_username,text)

    # 定位密码
    def page_input_password(self,text):
        self.base_input(Page.loc_pwd,text)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click_element(Page.loc_login_btn)