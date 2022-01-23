import time

import pytest

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
