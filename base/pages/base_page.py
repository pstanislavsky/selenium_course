from selenium.webdriver.common.by import By

from base.base_object import BaseObject
from components.cookie_banner import CookieBanner
from components.header import Header
from components.preloader import Preloader
from utils.xpath import has_class


class BasePage(BaseObject):
    """Базовый класс для страниц интернет-магазина."""

    def __init__(self, driver):
        self.driver = driver
        self.root = driver

    # Data
    URL = None

    # Locators
    PRELOADER_LOCATOR = (
        By.XPATH,
        f'//div[@id = "preloader" and {has_class("--active")}]',
    )
    HEADER_LOCATOR = (By.XPATH, f'//nav[{has_class("navbar")}]')
    COOKIE_BANNER_LOCATOR = (
        By.XPATH,
        f'//div[@id = "cookie-toast-container"]' f'//div[{has_class("toast")}]',
    )

    # Components
    @property
    def preloader(self):
        return Preloader(self, self.PRELOADER_LOCATOR)

    @property
    def header(self) -> Header:
        return Header(self, self.HEADER_LOCATOR)

    @property
    def cookie_banner(self):
        return CookieBanner(self, self.COOKIE_BANNER_LOCATOR)

    # Actions
    def open(self):
        """Открывает страницу в браузере."""

        self.driver.get(self.URL)

    def wait_opened(self, seconds=10):
        pass

    def wait_page_stable(self, seconds=3):
        """Ждёт стабилизацию страницы указанное время."""

        self.preloader.wait_until_loaded(appearance_timeout=seconds)
