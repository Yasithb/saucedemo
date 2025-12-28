import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")  # Browser opens per test case
def driver(request):
    options = Options()

    options.add_argument("--start-maximized")   # Open Chrome maximized
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")


    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(2)

    yield driver

    # Screenshot on failure
    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(f"screenshots/{request.node.name}.png")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
