from BaseApp1 import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time


# Создаем класс YandexSeacrhLocators с нашими локаторами
class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SUGGEST_TABLE = (By.XPATH, "//li[@data-index='1']")
    LOCATOR_YANDEX_SEARCH_REZULT = (By.ID, "search-result")
    LOCATOR_YANDEX_FIRST_URL = (By.XPATH, "//a[@accesskey='1']")


# Создаем класс SearchHelper на основе класса BasePage
class SearchHelper(BasePage):

    # Проверяем наличие поля поиска, м вводим в поиск "Тензор"
    def enter_word(self, word):
        time.sleep(3)
        search_input_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_input_field.click()
        search_input_field.send_keys(word)
        time.sleep(3)
        return search_input_field

    # Проверяем появилась ли таблица с подсказками (suggest)
    def check_table_suggest(self):
        search_suggest = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST_TABLE)
        time.sleep(3)
        return search_suggest

    # Нажимаем кнопку "ENTER"
    def click_button_enter(self):
        search_input = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)
        return search_input

    # Проверяем появилась ли страница результатов поиска
    def check_rezult(self):
        search_rezult = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_REZULT)
        time.sleep(3)
        return search_rezult

    # Проверяем, ведет ли 1-й результат из страницы результатов поиска на сайт "https://tensor.ru/"
    def check_first_url(self):
        search_first_url = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_FIRST_URL)
        return search_first_url.get_attribute("href")
