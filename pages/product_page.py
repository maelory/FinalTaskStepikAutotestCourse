from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_cta(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button isn't presented " \
                                                                                 "on page"

    def add_to_cart_click(self):
        addToCartCTA = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        addToCartCTA.click()

    def product_name_should_be_in_message(self):
        productName = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        productNameInAlert = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART_MESSAGE).text
        assert productName == productNameInAlert, f"Product name isn't in Add To Cart message. Should be " \
                                                  f"'{productName}', but '{productNameInAlert}' "

    def correct_price_should_be_in_message(self):
        productPrice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cartPrice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        assert productPrice == cartPrice, f"Product name isn't in Add To Cart message. Should be " \
                                                  f"'{productPrice}', but '{cartPrice}' "

    def add_to_cart_message_is_not_presented(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_CART_MESSAGE), "Add to cart message is " \
                                                                                         "presented on page, " \
                                                                                         "but shouldn't "

    def add_to_cart_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_CART_MESSAGE), "Add to cart message isn't " \
                                                                                  "disappeared "
