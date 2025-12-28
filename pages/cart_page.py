from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BTNS = (By.CSS_SELECTOR, ".cart_button")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BTN = (By.ID, "checkout")

    def get_title(self):
        return self.wait_for_visible(self.TITLE).text

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_first_item(self):
        self.driver.find_elements(*self.REMOVE_BTNS)[0].click()

    def remove_all_items(self):
        for btn in self.driver.find_elements(*self.REMOVE_BTNS):
            btn.click()

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

