from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import pytest_selenium
import time
from urllib.parse import urlparse


class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы и время ожидани элементов
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)


    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path