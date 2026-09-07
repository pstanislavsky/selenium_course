from selenium.common import TimeoutException

from base.components.base_component import BaseComponent


class Preloader(BaseComponent):
    # Actions
    def wait_until_loaded(self, appearance_timeout=3, disappearance_timeout=15):
        """Ожидает исчезновение прелоадера, если он появился."""

        try:
            self.wait_root_appear(appearance_timeout)
        except TimeoutException:
            return

        self.wait_root_disappear(disappearance_timeout)
