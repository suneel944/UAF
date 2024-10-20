from pytest import mark, fixture
from unittest.mock import MagicMock, patch
from selenium.webdriver.common.by import By
from uaf.utilities.ui.waiter.waits import Waits


@fixture
def mock_driver():
    return MagicMock()


@fixture
def mock_web_driver_wait():
    with patch("uaf.utilities.ui.waiter.waits.WebDriverWait") as mock:
        yield mock


@fixture
def mock_expected_conditions():
    with patch("uaf.utilities.ui.waiter.waits.EC") as mock:
        yield mock


@fixture
def mock_yaml_parser():
    with patch("uaf.utilities.ui.waiter.waits.YamlParser") as mock:
        mock_instance = mock.return_value
        mock_instance.get_value.return_value = 30
        yield mock


@fixture
def waits(mock_driver, mock_web_driver_wait, mock_yaml_parser):
    return Waits(mock_driver)


@mark.unit_test
def test_waits_init(waits, mock_driver, mock_web_driver_wait):
    assert waits.driver == mock_driver
    mock_web_driver_wait.assert_called_once_with(mock_driver, 30)


@mark.unit_test
def test_wait_for_element_to_be_clickable(waits, mock_expected_conditions):
    by_locator = (By.ID, "test_id")
    waits.wait_for_element_to_be_clickable(by_locator)
    waits.wait.until.assert_called_once_with(
        mock_expected_conditions.element_to_be_clickable(by_locator)
    )


@mark.unit_test
def test_wait_for_title(waits, mock_expected_conditions):
    title = "Test Title"
    waits.wait_for_title(title)
    waits.wait.until.assert_called_once_with(mock_expected_conditions.title_is(title))


@mark.unit_test
def test_wait_for_element_presence(waits, mock_expected_conditions):
    by_locator = (By.ID, "test_id")
    waits.wait_for_element_presence(by_locator)
    waits.wait.until.assert_called_once_with(
        mock_expected_conditions.presence_of_element_located(by_locator)
    )


@mark.unit_test
def test_wait_for_element_visibility(waits, mock_expected_conditions):
    by_locator = (By.ID, "test_id")
    waits.wait_for_element_visibility(by_locator)
    waits.wait.until.assert_called_once_with(
        mock_expected_conditions.visibility_of_element_located(by_locator)
    )


@mark.unit_test
def test_wait_for_until(waits):
    def custom_condition(x):
        return True

    waits.wait_for_until(custom_condition)
    waits.wait.until.assert_called_once_with(custom_condition)


@mark.unit_test
def test_wait_for_page_load(waits, mock_driver):
    mock_driver.execute_script.return_value = "complete"
    waits.wait_for_page_load()
    assert mock_driver.execute_script.call_count == 1
    assert waits.wait.until.call_count == 1
