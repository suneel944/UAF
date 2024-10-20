from pytest import mark, fixture
from unittest.mock import MagicMock
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from uaf.utilities.ui.locator.locator_utils import LocatorUtils


@fixture
def mock_driver():
    driver = MagicMock()
    driver.find_element.return_value = MagicMock()
    driver.find_elements.return_value = [MagicMock(), MagicMock()]
    return driver


@fixture
def locator_utils(mock_driver):
    return LocatorUtils(mock_driver)


@mark.unit_test
def test_locator_utils_init(locator_utils, mock_driver):
    assert locator_utils.driver == mock_driver


@mark.unit_test
def test_by_locator_to_web_element(locator_utils, mock_driver):
    by_locator = (By.ID, "test_id")
    element = locator_utils.by_locator_to_web_element(by_locator)
    mock_driver.find_element.assert_called_once_with(By.ID, "test_id")
    assert element == mock_driver.find_element.return_value


@mark.unit_test
def test_by_locator_to_mobile_element(locator_utils, mock_driver):
    by_locator = (AppiumBy.ACCESSIBILITY_ID, "test_accessibility_id")
    element = locator_utils.by_locator_to_mobile_element(by_locator)
    mock_driver.find_element.assert_called_once_with(
        AppiumBy.ACCESSIBILITY_ID, "test_accessibility_id"
    )
    assert element == mock_driver.find_element.return_value


@mark.unit_test
def test_by_locator_to_web_elements(locator_utils, mock_driver):
    by_locator = (By.CLASS_NAME, "test_class")
    elements = locator_utils.by_locator_to_web_elements(by_locator)
    mock_driver.find_elements.assert_called_once_with(By.CLASS_NAME, "test_class")
    assert elements == mock_driver.find_elements.return_value
    assert len(elements) == 2


@mark.unit_test
def test_perform_by_to_element_conversion(locator_utils, mock_driver):
    by_locator = (By.NAME, "test_name")
    element = locator_utils._LocatorUtils__perform_by_to_element_conversion(by_locator)
    mock_driver.find_element.assert_called_once_with(By.NAME, "test_name")
    assert element == mock_driver.find_element.return_value
