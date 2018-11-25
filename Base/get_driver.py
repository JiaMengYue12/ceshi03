def getdriver():
    from appium import webdriver

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'emulator-5554'
    # com.vcooline.aike/.umanager.LoginActivity
    desired_caps['appPackage'] = 'com.vcooline.aike'
    desired_caps['appActivity'] = '.umanager.LoginActivity'


    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)