from webdriver import BasePage
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    search_field = (By.ID, "text")
    search_button = (By.CLASS_NAME, "search3__button")
    nav_bar = (By.CLASS_NAME, "services-suggest__icons-more")
    suggest_menu = (By.CLASS_NAME, "mini-suggest__popup-content")
    first_result = (By.XPATH, "//*[@id='search-result']/li[1]/div/div[2]/div[1]/a/b")
    images = (By.CSS_SELECTOR, "[aria-label='Картинки']")
    first_category = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    text_first_category = (By.CLASS_NAME, "PopularRequestList-SearchText")
    input = (By.CLASS_NAME, "input__control")
    first_image = (By.CLASS_NAME, "serp-item_pos_0")
    text_image = (By.CLASS_NAME, "MMOrganicSnippet-Title")
    next_button = (By.CLASS_NAME, "CircleButton_type_next")
    prev_button = (By.CLASS_NAME, "CircleButton_type_prev")


class Helper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.search_field)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSearchLocators.search_button, time=2).click()

    def find_suggest_menu(self):
        return self.find_element(YandexSearchLocators.suggest_menu, time=2)

    def get_first_result_link(self):
        return self.find_element(YandexSearchLocators.first_result).text

    def check_images(self):
        self.find_element(YandexSearchLocators.search_field).click()
        self.find_element(YandexSearchLocators.nav_bar, time=2).click()
        self.find_element(YandexSearchLocators.images, time=2)

    def go_to_first_category(self):
        self.find_element(YandexSearchLocators.first_category, time=2).click()
        return self.find_element(YandexSearchLocators.text_first_category, time=2).text

    def get_input(self):
        return self.find_element(YandexSearchLocators.input).get_attribute("value")

    def go_to_first_image(self):
        self.find_element(YandexSearchLocators.first_image).click()
        return self.find_element(YandexSearchLocators.text_image).text

    def go_to_second_image(self):
        self.find_element(YandexSearchLocators.next_button).click()
        return self.find_element(YandexSearchLocators.text_image).text

    def return_image(self):
        self.find_element(YandexSearchLocators.prev_button).click()
        return self.find_element(YandexSearchLocators.text_image).text
