from YandexPages import SearchHelper


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.maximize_window()
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.check_table_suggest()
    yandex_main_page.click_button_enter()
    yandex_main_page.check_rezult()
    url = yandex_main_page.check_first_url()
    assert url == "https://tensor.ru/"
