from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создаем класс и инициализируем его
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    # Этот метод увеличивает окно браузера до максимального
    def maximize_window(self):
        return self.driver.maximize_window()

    # Этот метод находит элемент на странице
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не удается найти элемент по локатору {locator}")

    # Этот метод открывает окно браузера и переходит на заданный url
    def go_to_site(self):
        return self.driver.get(self.base_url)
