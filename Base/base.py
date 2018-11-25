from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver=driver

    # 查找元素
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).\
            until(lambda x:x.find_element(*loc))

    # 点击元素
    def base_click_element(self,loc):
        self.base_find_element(loc).click()


    # 输入内容
    def base_input(self,loc,text):
        el=self.base_find_element(loc).clear().send_keys(text)
        # el.clear()
        # el.send_keys(text)


# from selenium.webdriver.common.by import By
#
# loc=By.XPATH,"//*[contains(@text,'WLAN')]"
# print(type(loc))   #打印出来的是元组
# print(loc)  # 打印的是 ('xpath', "//*[contains(@text,'WLAN')]")
# print(*loc)  # 打印的是 xpath //*[contains(@text,'WLAN')]
