from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def cart_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Basket should be empty"

    def cart_should_not_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Basket should not be empty"

    def empty_cart_message_should_be_displayed(self):
        emptyBasketMessage = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty." in emptyBasketMessage, "Empty basket message isn't displayed"
