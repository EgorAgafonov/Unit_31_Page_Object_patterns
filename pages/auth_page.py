import os
import time

from .base_page import BasePage
from .locators import AuthLocators


class AuthPage(BasePage):

    def __init__(self, driver, timeout=2):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://petfriends.skillfactory.ru/login"
        driver.get(url)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        time.sleep(2)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()
