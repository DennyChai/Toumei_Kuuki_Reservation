from selenium.webdriver.chrome.service import Service
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from typing import Union


class Provider(object):
    def __init__(self, send_msg) -> None:
        self.send_msg = send_msg

    def get_driver(self) -> Union[webdriver.Chrome, None]:
        try:
            capabilities = DesiredCapabilities.CHROME
            capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")  # 是否driver控制瀏覽器
            options.add_argument("--incognito")  # 無痕設定
            options.add_argument("ignore-certificate-errors")
            options.add_argument("--disable-gpu")  # 規避google bug
            options.add_experimental_option("detach", True)  # 持續開著
            options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 關閉除錯LOG(selenium自帶的,並非程式碼錯誤)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 開發者模式
            webdriver_path = Service("./chromedriver")  # Selenium路徑
            return self.check_driver_version(capabilities, options, webdriver_path)
        except:
            self.send_msg()
            return None

    def check_driver_version(
        self, capabilities: DesiredCapabilities, options: webdriver.ChromeOptions, webdriver_path: Service
    ) -> Union[webdriver.Chrome, None]:
        driver = None
        try:
            driver = webdriver.Chrome(desired_capabilities=capabilities, options=options, service=webdriver_path)
        except:
            self.send_msg()
        return driver
