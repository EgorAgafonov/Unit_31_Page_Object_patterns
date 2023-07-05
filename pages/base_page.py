from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import pytest_selenium
import time
from urllib.parse import urlparse



# PageObject (иногда Page Object Model, POM) — это паттерн программирования, основанный на идее создания отдельных
# программных объектов, в которых будут скрыты все методы по работе с конкретной страницей. Мы разделяем логику теста
# и специфику работы с HTML-элементами. Таким образом, тесты работают с интерфейсом через объекты PageObject,
# абстрагируясь от конкретной реализации в HTML-коде.


class BasePage(object):
    """Базовый класс для предполагаемой, абстрактной страницы в рамках изучения темы Page object."""

    def __init__(self, driver, url, timeout=2):
        """Метод __init__ будет запускать в момент создания объекта из класса и устанавливать нужные свойства.
        driver.implicitly_wait(10) — задаёт максимальное время ожидания в секундах, в течении которого WebDriver
         пытается найти элемент, если он недоступен сразу же."""

        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        """Метод get_relative_link возвращает относительный путь до текущей страницы (без домена). Он будет полезен
        для понимания того, на какой странице мы сейчас находимся при редиректах от сервера или при отправке форм
        при нажатиях кнопки авторизации. При этом мы не хотим зависеть от текущего домена сайта, дополнительных
        get-параметров или протокола (http или https) и проверяем только часть url, содержащую путь к файлу.
        Для этого нам необходима библиотека urllib."""

        url = urlparse(self.driver.current_url)
        return url.path
