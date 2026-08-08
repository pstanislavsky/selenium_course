from selenium.webdriver.remote.webelement import WebElement

from base.base_object import BaseObject


class BaseComponent(BaseObject):
    """Базовый класс для компонентов веб-страниц."""

    def __init__(self, parent, root_locator):
        self.parent = parent
        self.driver = parent.driver
        self.root_locator = root_locator

    # Properties
    @property
    def root(self) -> WebElement:
        return self.parent.get_element(self.root_locator)

    @property
    def is_displayed(self) -> bool:
        return self.parent.is_visible(self.root_locator)

    # Actions
    def wait_root_appear(self, timeout=10):
        """Ожидает появление компонента."""

        self.parent.get_element(self.root_locator, timeout)

    def wait_root_disappear(self, timeout=10):
        """Ожидает исчезновение компонента."""

        self.parent.wait_until_not_visible(self.root_locator, timeout)

    def wait_page_stable(self, seconds=2):
        """Ждёт стабилизацию страницы указанное время."""

        self.parent.wait_page_stable(seconds)
