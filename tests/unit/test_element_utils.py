from pytest import mark, fixture
from unittest.mock import MagicMock, patch
from selenium.webdriver.common.by import By

from uaf.utilities.ui.element.element_utils import ElementUtils


@fixture
def mock_driver():
    return MagicMock()


@fixture
def element_utils(mock_driver):
    return ElementUtils(mock_driver)


@mark.unit_test
def test_element_utils_init(element_utils):
    assert element_utils.driver is not None
    assert element_utils.wait is not None
    assert element_utils.locator is not None


@mark.unit_test
@patch(
    "uaf.utilities.ui.locator.locator_utils.LocatorUtils.by_locator_to_mobile_element"
)
def test_click_on_element_using_js(mock_by_locator, element_utils):
    by_locator = (By.ID, "test_id")
    mock_element = MagicMock()
    mock_by_locator.return_value = mock_element

    element_utils.click_on_element_using_js(by_locator)

    element_utils.driver.execute_script.assert_called_once_with(
        "arguments[0].click();", mock_element
    )


@mark.unit_test
@patch("uaf.utilities.ui.waiter.waits.Waits.wait_for_element_to_be_clickable")
def test_click_on_element(mock_wait_for_clickable, element_utils):
    by_locator = (By.ID, "test_id")
    mock_element = MagicMock()
    mock_wait_for_clickable.return_value = mock_element

    element_utils.click_on_element(by_locator)

    mock_wait_for_clickable.assert_called_once_with(by_locator)
    mock_element.click.assert_called_once()


@mark.unit_test
@patch("uaf.utilities.ui.waiter.waits.Waits.wait_for_page_load")
def test_launch_url(mock_wait_for_page_load, element_utils):
    url = "https://example.com"
    element_utils.launch_url(url)
    element_utils.driver.get.assert_called_once_with(url)
    mock_wait_for_page_load.assert_called_once()


@mark.unit_test
@patch("uaf.utilities.ui.waiter.waits.Waits.wait_for_title")
def test_fetch_title(mock_wait_for_title, element_utils):
    title = "Test Title"
    element_utils.driver.title = title

    result = element_utils.fetch_title(title)

    mock_wait_for_title.assert_called_once_with(title)
    assert result == title


@mark.unit_test
@patch("uaf.utilities.ui.locator.locator_utils.LocatorUtils.by_locator_to_web_element")
@patch("time.sleep")
def test_send_keys(mock_sleep, mock_by_locator, element_utils):
    by_locator = (By.ID, "test_id")
    text = "test text"
    mock_element = MagicMock()
    mock_by_locator.return_value = mock_element

    element_utils.send_keys(by_locator, text)
    mock_element.send_keys.assert_called_once_with(text)

    element_utils.send_keys(by_locator, text, enter_char_by_char=True)
    assert mock_element.send_keys.call_count == len(text) + 1
    assert mock_sleep.call_count == len(text)


@mark.unit_test
@patch("uaf.utilities.ui.locator.locator_utils.LocatorUtils.by_locator_to_web_element")
def test_get_text_from_element(mock_by_locator, element_utils):
    by_locator = (By.ID, "test_id")
    expected_text = "Test Text"
    mock_element = MagicMock()
    mock_element.text = expected_text
    mock_by_locator.return_value = mock_element

    result = element_utils.get_text_from_element(by_locator)

    assert result == expected_text


@mark.unit_test
@patch("uaf.utilities.ui.locator.locator_utils.LocatorUtils.by_locator_to_web_element")
@patch("uaf.utilities.ui.element.element_utils.Select")
def test_select_from_drop_down(mock_select, mock_by_locator, element_utils):
    by_locator = (By.ID, "test_id")
    value = "option1"
    mock_element = MagicMock()
    mock_by_locator.return_value = mock_element

    element_utils.select_from_drop_down(by_locator, value)

    mock_select.assert_called_once_with(mock_element)
    mock_select.return_value.select_by_value.assert_called_once_with(value)
