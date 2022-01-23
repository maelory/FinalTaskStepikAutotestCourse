import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_cta()
    page.add_to_cart_click()
    page.solve_quiz_and_get_code()
    page.product_name_should_be_in_message()
    page.correct_price_should_be_in_message()
