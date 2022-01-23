import time

import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
url_list = [base_url + "?promo=offer" + str(n) for n in range(0, 10)]
url_list_with_xfail = [pytest.param(url, marks=pytest.mark.xfail) if url[-1] == "7" else url for url in url_list]


@pytest.mark.parametrize('url', url_list_with_xfail)
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.should_be_add_to_cart_cta()
    page.add_to_cart_click()
    page.solve_quiz_and_get_code()
    page.product_name_should_be_in_message()
    page.correct_price_should_be_in_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_add_to_cart_cta()
    page.add_to_cart_click()
    page.solve_quiz_and_get_code()
    page.add_to_cart_message_is_not_presented()


def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart_message_is_not_presented()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_add_to_cart_cta()
    page.add_to_cart_click()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.add_to_cart_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
