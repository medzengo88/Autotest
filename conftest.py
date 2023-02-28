import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(
        executable_path=r'C:\Users\Rail\PycharmProjects\test_tenzor\chromedriver\chromedriver.exe')
    yield driver
    driver.quit()
