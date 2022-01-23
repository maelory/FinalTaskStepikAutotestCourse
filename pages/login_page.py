from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        registrationEmail = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_ADDRESS)
        registrationEmail.send_keys(email)
        registrationPassword = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        registrationPassword.send_keys(password)
        registrationConfirmPassword = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        registrationConfirmPassword.send_keys(password)
        registrationButton = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registrationButton.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "URL isn't correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_ADDRESS), "Login email address is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Log In button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_ADDRESS), "Register email address is not " \
                                                                                   "presented "
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), "Register confirm password is " \
                                                                                      "not presented "
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"
