from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def should_be_success_message(self):
        assert self.is_element_present(*MainPageLocators.MESSAGE_AFTER_SUCCESS_REGISTRATION), 'Message after success fegistration is not present'
        assert True
