from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    CANCEL_BTN = (By.ID, "cancel")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    FINISH_BTN = (By.ID, "finish")

    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BTN = (By.ID, "back-to-products")

    def fill_checkout_info(self, first, last, zip_code):
        if first is not None:
            self.type(self.FIRST_NAME, first)
        if last is not None:
            self.type(self.LAST_NAME, last)
        if zip_code is not None:
            self.type(self.POSTAL_CODE, zip_code)


        self.click(self.CONTINUE_BTN)
        self.wait.until(EC.url_contains("checkout-step-two"))

    def is_on_step_one(self):
        return "checkout-step-one" in self.driver.current_url

    def is_on_step_two(self):
        self.wait.until(EC.url_contains("checkout-step-two"))
        return self.wait.until(EC.visibility_of_element_located(self.FINISH_BTN)).is_displayed()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG)).text

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def click_cancel(self):
        self.click(self.CANCEL_BTN)
        self.wait.until(EC.url_contains("cart"))

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG)).text

    def click_back_home(self):
        self.click(self.BACK_HOME_BTN)
