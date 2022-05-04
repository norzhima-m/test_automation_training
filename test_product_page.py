from .pages.product_page import ProdactPage
from time import sleep

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProdactPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_alert_with_name_book()
    page.should_be_alert_with_price()
    # sleep(10)
