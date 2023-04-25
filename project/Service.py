from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


class Service(object):
    def __init__(self, inputs) -> None:
        self.send_msg = inputs["send_msg"]
        self.provider = inputs["provider"]
        self.book_info = inputs["book_info"]

    def flow_service(self):
        gender_mapping = {"男生": "gender-male", "女生": "gender-female"}
        driver = self.provider.get_driver()
        driver.get(
            "https://inline.app/booking/-My6-cd2DzEiovrnGB9j:inline-live-2/-My6-csbwZpGlP_tDN7I?language=zh-tw"
        )  # 透明空氣網址
        driver.execute_script("window.scrollTo(0, 1800)")
        time.sleep(10)
        # 選大人人數
        adults_numbers = Select(
            wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="adult-picker"]')))
        )
        adults_numbers.select_by_value(self.book_info["adults"])
        # 選小孩人數
        child_numbers = Select(wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kid-picker"]'))))
        child_numbers.select_by_value(self.book_info["childrens"])
        # 將月曆選擇器展開
        wait(driver, 60).until(EC.element_to_be_clickable((By.ID, "date-picker"))).click()
        # 選日期
        wait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[@data-date="{self.book_info["date"]}"]'))
        ).click()
        time.sleep(1)
        # 選時間
        wait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, f'//button/span[contains(text(), "{self.book_info["time"]}")]'))
        ).click()

        # 點下一步, 填寫聯絡資訊
        wait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-cy="book-now-action-button"]'))
        ).click()
        # 要往下滑, 才能點按鈕
        wait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="markdown"]//p[contains(text(), "交通資訊")]'))
        ).click()
        # 點選我已閱讀並同意注意事項
        wait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-cy="confirm-house-rule"]'))
        ).click()
        # 輸入姓名
        wait(driver, 15).until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(self.book_info["name"])
        # 選先生 OR 小姐
        wait(driver, 15).until(EC.element_to_be_clickable((By.ID, gender_mapping[self.book_info["sex"]]))).click()
        # 輸入手機
        wait(driver, 15).until(EC.element_to_be_clickable((By.ID, "phone"))).send_keys(
            self.book_info["contact_number"]
        )
        # 輸入Email
        wait(driver, 15).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(self.book_info["email"])
        # 勾選我已閱讀並同意
        wait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="privacy-policy"]'))).click()

        # 最後送出
        wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()  # 確定定位
