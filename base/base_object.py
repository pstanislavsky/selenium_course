from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseObject:
    """Базовый класс для взаимодействия с веб-элементами."""

    driver: WebDriver
    root: WebDriver | WebElement

    def get_element(self, locator, timeout=10, poll_frequency=0.1) -> WebElement:
        """Возвращает видимый элемент."""

        return WebDriverWait(self.root, timeout, poll_frequency).until(
            EC.visibility_of_element_located(locator)
        )

    def get_elements(self, locator, timeout=10, poll_frequency=0.1) -> list[WebElement]:
        """Возвращает все видимые элементы."""

        return WebDriverWait(self.root, timeout, poll_frequency).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def get_text(self, locator, timeout=10, poll_frequency=0.1) -> str:
        """Возвращает очищенный текст видимого элемента."""

        return self.get_element(locator, timeout, poll_frequency).text.strip()

    def get_direct_text(self, locator, timeout=10, poll_frequency=0.1) -> str:
        """Возвращает очищенный текст элемента без текста его потомков."""

        return self.driver.execute_script(
            '''
            return Array.from(arguments[0].childNodes)
                .filter(node => node.nodeType === Node.TEXT_NODE)
                .map(node => node.textContent)
                .join('')
                .replace(/\\s+/g, ' ');
            ''',
            self.get_element(locator, timeout, poll_frequency),
        ).strip()

    def wait_until_not_visible(self, locator, timeout=10, poll_frequency=0.1):
        """Ожидает, пока элемент перестанет отображаться."""

        WebDriverWait(self.root, timeout, poll_frequency).until(
            EC.invisibility_of_element_located(locator)
        )

    def is_visible(self, locator, timeout=1, poll_frequency=0.1) -> bool:
        """Проверяет, отображается ли элемент на странице."""

        try:
            self.get_element(locator, timeout, poll_frequency)
            return True
        except TimeoutException:
            return False

    def is_not_visible(self, locator, timeout=1, poll_frequency=0.1) -> bool:
        """Проверяет, не отображается ли элемент на странице."""

        try:
            self.wait_until_not_visible(locator, timeout, poll_frequency)
            return True
        except TimeoutException:
            return False

    def get_present_element(
        self, locator, timeout=10, poll_frequency=0.1
    ) -> WebElement:
        return WebDriverWait(self.root, timeout, poll_frequency).until(
            EC.presence_of_element_located(locator)
        )

    def is_present(self, locator, timeout=1, poll_frequency=0.1) -> bool:
        try:
            self.get_present_element(locator, timeout, poll_frequency)
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator, timeout=10, poll_frequency=0.1):
        """Прокручивает страницу к указанному элементу."""

        self.driver.execute_script(
            '''
            arguments[0].scrollIntoView({
                block: "center", 
                inline: "nearest", 
                behavior: "instant"
            });
            ''',
            self.get_element(locator, timeout, poll_frequency),
        )

    def click_element(self, locator, timeout=10, poll_frequency=0.1):
        """Нажимает на указанный элемент."""

        self.scroll_to_element(locator, timeout, poll_frequency)

        WebDriverWait(self.root, timeout, poll_frequency).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def hover_element(self, locator, timeout=10, poll_frequency=0.1):
        """Наводит курсор на указанный элемент."""

        self.scroll_to_element(locator, timeout, poll_frequency)

        ActionChains(self.driver).move_to_element(
            self.get_element(locator, timeout, poll_frequency)
        ).perform()

    def enter_text(self, locator, value, timeout=10, poll_frequency=0.1):
        """Вводит текст в указанное поле."""

        self.scroll_to_element(locator, timeout, poll_frequency)

        element = self.get_element(locator, timeout, poll_frequency)
        element.clear()
        element.send_keys(value)

    def enter_text_and_submit(self, locator, value, timeout=10, poll_frequency=0.1):
        """Вводит текст в указанное поле и нажимает кнопку Return."""

        self.enter_text(locator, value, timeout, poll_frequency)
        self.get_element(locator, timeout, poll_frequency).send_keys(Keys.RETURN)

    def drag_element_by_offset(
        self, locator, x_offset, y_offset, timeout=10, poll_frequency=0.1
    ):
        """Перетаскивает указанный элемент на заданное смещение."""

        self.scroll_to_element(locator, timeout, poll_frequency)

        ActionChains(self.driver).click_and_hold(
            self.get_element(locator, timeout, poll_frequency)
        ).move_by_offset(x_offset, y_offset).release().perform()

    def drag_horizontally_to_element(
        self,
        container_locator,
        target_locator,
        drag_step=200,
        max_attempts=10,
        tolerance=1,
        timeout=10,
        poll_frequency=0.1,
    ):
        for _ in range(max_attempts):
            container_rect = self.get_element(
                container_locator, timeout, poll_frequency
            ).rect
            target_rect = self.get_present_element(
                target_locator, timeout, poll_frequency
            ).rect

            container_left = container_rect['x']
            container_right = container_left + container_rect['width']

            target_left = target_rect['x']
            target_right = target_left + target_rect['width']

            if target_left < container_left - tolerance:
                x_offset = drag_step
            elif target_right > container_right + tolerance:
                x_offset = -drag_step
            else:
                return

            self.drag_element_by_offset(
                container_locator,
                x_offset=x_offset,
                y_offset=0,
                timeout=timeout,
                poll_frequency=poll_frequency,
            )

        raise TimeoutException(
            f'Element could not be dragged into view: {target_locator}.'
        )
