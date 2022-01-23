from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_BUTTON = (By.XPATH, "//button[@name='login_submit']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1")
    PRODUCT_IN_CART_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]/div[@class='alertinner ']/strong")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_PRICE_IN_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
