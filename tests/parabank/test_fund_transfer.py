from tests.fixtures.conftest import web_driver
from pytest import mark
from uaf.enums.browser_make import WebBrowserMake
from selenium.webdriver.common.by import By
from uaf.utilities.ui.waiter.waits import Waits


@mark.parametrize(
    "web_driver", [{"arg_browser_make": WebBrowserMake.CHROME}], indirect=True
)
def test_fund_transfer(web_driver):
    waiter = Waits(web_driver)
    web_driver.get("https://parabank.parasoft.com/parabank/index.htm")
    web_driver.find_element(By.XPATH, ".//*[@type='text'][@name='username']").send_keys(
        "test_1"
    )
    web_driver.find_element(
        By.XPATH, ".//*[@type='password'][@name='password']"
    ).send_keys("demo")
    web_driver.find_element(By.XPATH, ".//*[@type='submit']").click()
    waiter.wait_for_element_visibility(
        (By.XPATH, ".//a[text()='Transfer Funds']")
    ).click()
