from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def login(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")


# TC01 – Verify Products page navigation

def test_products_page_navigation(driver):
    login(driver)
    products = ProductsPage(driver)
    assert products.get_title() == "Products"


# TC02 – Verify products are displayed

def test_products_displayed(driver):
    login(driver)
    products = ProductsPage(driver)
    assert products.get_products_count() > 0


# TC03 – Sort by Price (Low → High)

def test_sort_price_low_to_high(driver):
    login(driver)
    products = ProductsPage(driver)

    products.sort_by_value("lohi")
    prices = products.get_prices()

    assert prices == sorted(prices)


# TC04 – Sort by Price (High → Low)

def test_sort_price_high_to_low(driver):
    login(driver)
    products = ProductsPage(driver)

    products.sort_by_value("hilo")
    prices = products.get_prices()

    assert prices == sorted(prices, reverse=True)


# TC05 – Add single product to cart

def test_add_single_product(driver):
    login(driver)
    products = ProductsPage(driver)

    products.add_products(1)
    assert products.get_cart_count() == "1"


# TC06 – Add multiple products to cart

def test_add_multiple_products(driver):
    login(driver)
    products = ProductsPage(driver)

    products.add_products(2)
    assert products.get_cart_count() == "2"


# TC07 – Remove product from product page

def test_remove_product(driver):
    login(driver)
    products = ProductsPage(driver)

    products.add_products(1)
    products.remove_first_product()

    # Cart badge disappears after removal
    assert len(driver.find_elements(*ProductsPage.CART_BADGE)) == 0


# TC08 – Navigate to cart page

def test_navigate_to_cart(driver):
    login(driver)
    products = ProductsPage(driver)

    products.go_to_cart()
    assert "cart" in driver.current_url


# TC09 – Logout from product page

def test_logout_from_products_page(driver):
    login(driver)
    products = ProductsPage(driver)

    products.logout()
    assert "saucedemo.com" in driver.current_url
