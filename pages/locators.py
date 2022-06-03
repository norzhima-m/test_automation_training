from selenium.webdriver.common.by import By


class MainPageLocators():
    MESSAGE_AFTER_SUCCESS_REGISTRATION = (By.CSS_SELECTOR, "#messages")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT_WITH_NAME_BOOK = (By.CSS_SELECTOR, '#messages div:first-child strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ALERT_WITH_PRICE = (By.CSS_SELECTOR, '#messages .alert-info strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:first-child div')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")

    
