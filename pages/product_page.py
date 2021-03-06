from audioop import add
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
    
    def should_be_alert_with_name_book(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text   
        alert_name_book = self.browser.find_element(*ProductPageLocators.ALERT_WITH_NAME_BOOK).text
        assert product_name == alert_name_book, f'Book "{product_name}" has not been added to the cart'

    def should_be_alert_with_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_WITH_PRICE).text
        assert product_price == alert_price, "Price is incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is present, but should not be."

    def message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

        


