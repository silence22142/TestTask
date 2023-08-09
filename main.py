import pytest
from selenium import webdriver
from YandexPage import Helper


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_yandex_search(browser):
    yandex_main_page = Helper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.find_suggest_menu()
    yandex_main_page.click_on_the_search_button()
    assert "tensor.ru" == yandex_main_page.get_first_result_link()


def test_yandex_images(browser):
    yandex_page = Helper(browser)
    yandex_page.go_to_site("https://ya.ru/")
    yandex_page.check_images()
    yandex_page.go_to_site("https://ya.ru/images")
    assert yandex_page.go_to_first_category() == yandex_page.get_input()
    text = yandex_page.go_to_first_image()
    assert text != yandex_page.go_to_second_image()
    assert text == yandex_page.return_image()
