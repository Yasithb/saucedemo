from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class ProductsPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BTNS = (By.CSS_SELECTOR, ".inventory_item button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PRICES = (By.CLASS_NAME, "inventory_item_price")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")

    def get_title(self):
        return self.wait_for_visible(self.TITLE).text

    def get_products_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def sort_by_value(self, value):
        Select(self.wait_for_visible(self.SORT_DROPDOWN)).select_by_value(value)

    def add_products(self, count=1):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTNS)
        for i in range(count):
            buttons[i].click()

    def remove_first_product(self):
        self.driver.find_elements(*self.ADD_TO_CART_BTNS)[0].click()

    def get_cart_count(self):
        return self.wait_for_visible(self.CART_BADGE).text

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_prices(self):
        return [float(p.text.replace("$", "")) for p in self.driver.find_elements(*self.PRICES)]

    def get_product_names(self):
        return [n.text for n in self.driver.find_elements(*self.ITEM_NAMES)]

    def logout(self):
        self.click(self.MENU_BTN)
        self.click(self.LOGOUT_BTN)
