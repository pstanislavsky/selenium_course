from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseObject:
    """Базовый класс для веб-объектов."""

    # Локаторы
    PAGE_PRELOADER_LOCATOR = (By.XPATH, '//div[@id="preloader" and contains(@class, "--active")]')

    def __init__(self, root):
        self.root = root

    @property
    def driver(self):
        if isinstance(self.root, WebElement):
            return self.root.parent

        return self.root

    # Геттеры
    def get_element(self, locator, timeout=10):
        """Возвращает видимый элемент."""

        return WebDriverWait(self.root, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_text(self, locator, timeout=10):
        """Возвращает текст видимого элемента."""

        return self.get_element(locator, timeout).text

    def is_visible(self, locator, timeout=10):
        """Проверяет, отображается ли элемент на странице."""

        try:
            self.get_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    # Действия
    def click_element(self, locator, timeout=10):
        """Нажимает на указанный элемент."""

        WebDriverWait(self.root, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def safe_click_element(self, locator, timeout=10, attempts=5):
        """"Нажимает на указанный элемент после исчезновения прелоадера."""

        for attempt in range(attempts):
            self.wait_preloader_disappear()
            try:
                self.click_element(locator, timeout)
                return
            except ElementClickInterceptedException:
                if attempt == attempts - 1:
                    raise

    def enter_text(self, locator, value, timeout=10):
        """Вводит текст в указанное поле."""

        WebDriverWait(self.root, timeout).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(value)

    def wait_preloader_disappear(self, timeout=10):
        """Ждёт исчезновения прелоадера."""

        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(self.PAGE_PRELOADER_LOCATOR)
        )