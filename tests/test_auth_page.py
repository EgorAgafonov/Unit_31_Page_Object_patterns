from pages.auth_page import AuthPage
import time


def test_auth_page(selenium):
    page = AuthPage(selenium)
    page.enter_email("fonovagafonov@yandex.ru")
    time.sleep(2)
    page.enter_pass("123456")
    time.sleep(2)
    page.btn_click()

    assert page.get_relative_link() == '/all_pets', "login error"
