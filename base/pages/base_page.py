from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from base.base_object import BaseObject
from components.cookie_banner import CookieBanner
from components.header import Header
from components.modals.login_modal import LoginModal
from components.preloader import Preloader
from utils.xpath import has_class


class BasePage(BaseObject):
    """Базовый класс для страниц интернет-магазина."""

    # Data
    URL = None

    def __init__(self, driver):
        self.driver = driver
        self.root = driver

    # Locators
    PRELOADER_LOCATOR = (
        By.XPATH,
        f'//div[@id = "preloader" and {has_class("--active")}]',
    )
    HEADER_LOCATOR = (By.XPATH, f'//nav[{has_class("navbar")}]')
    LOGIN_MODAL_LOCATOR = (
        By.XPATH,
        f'//div[@id = "systemAuthAuthorizeModal"]'
        f'//div[{has_class("modal-content")}]',
    )
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
    def login_modal(self):
        return LoginModal(self, self.LOGIN_MODAL_LOCATOR)

    @property
    def cookie_banner(self):
        return CookieBanner(self, self.COOKIE_BANNER_LOCATOR)

    # Actions
    def open(self):
        """Открывает страницу в браузере."""

        self.driver.get(self.URL)

    def wait_opened(self, seconds=10):
        pass

    def wait_page_stable(self, seconds=2):
        """Ждёт стабилизацию страницы указанное время."""

        self.preloader.wait_until_loaded(appearance_timeout=seconds)

    def log_in(self, login, password):
        self.header.open_login_modal()
        self.login_modal.wait_root_appear()
        self.login_modal.log_in(login, password)
