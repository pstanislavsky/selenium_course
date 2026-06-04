from time import sleep

from selenium.webdriver.common.by import By

from base.base_object import BaseObject
from components.header import Header


class BasePage(BaseObject):
    """Базовый класс для страниц интернет-магазина."""

    # Данные
    PAGE_URL = None
    PAGE_TITLE = None

    # Локаторы
    PAGE_TITLE_LOCATOR = None
    HEADER_LOCATOR = (By.XPATH, '//nav[contains(@class, "navbar")]')

    @property
    def header(self):
        return Header(self.get_element(self.HEADER_LOCATOR))

    # Геттеры
    def open(self):
        """Открывает страницу в браузере."""

        self.driver.get(self.PAGE_URL)

    # Действия
    def wait(self, seconds):
        """Ждёт указанное время."""

        sleep(seconds)

    # Методы
    def should_be_opened(self):
        """Проверяет URL и заголовок открытой страницы."""

        page_url = self.driver.current_url
        assert page_url == self.PAGE_URL, (f'Некорректный URL страницы: получено "{page_url}", '
                                           f'ожидалось "{self.PAGE_URL}".')

        page_title = self.get_text(self.PAGE_TITLE_LOCATOR)
        assert page_title == self.PAGE_TITLE, (f'Некорректный заголовок страницы: получено "{page_title}", '
                                               f'ожидалось "{self.PAGE_TITLE}".')

        print(f'Открыта страница "{page_title}".')