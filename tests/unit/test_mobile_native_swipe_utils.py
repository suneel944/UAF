from pytest import mark, fixture, raises
from unittest.mock import MagicMock, patch
from selenium.common.exceptions import NoSuchElementException
from uaf.utilities.ui.swipe.swipe_utils import SwipeUtils
from uaf.enums.direction import Direction


@fixture
def mock_driver():
    return MagicMock()


@fixture
def swipe_utils(mock_driver):
    return SwipeUtils(mock_driver)


@mark.unit_test
def test_swipe_utils_init(swipe_utils):
    assert swipe_utils.driver is not None
    assert swipe_utils.finger is not None
    assert swipe_utils.locator is not None
    assert swipe_utils.actions is not None


@mark.unit_test
@patch("selenium.webdriver.common.action_chains.ActionChains.perform")
def test_swipe_till_text_visibility(mock_perform, swipe_utils, mock_driver):
    mock_driver.get_window_size.return_value = {"width": 1080, "height": 1920}
    mock_driver.page_source = "<div>Some other text</div>"

    def side_effect(*args, **kwargs):
        if mock_perform.call_count == 2:
            mock_driver.page_source = "<div>WhatsApp</div>"

    mock_perform.side_effect = side_effect
    swipe_utils.swipe_till_text_visibility("WhatsApp", Direction.DOWN, max_swipe=3)
    assert "WhatsApp" in mock_driver.page_source
    assert mock_perform.call_count == 2


@mark.unit_test
def test_swipe_till_text_visibility_invalid_max_swipe(swipe_utils):
    with raises(ValueError, match="max_swipe must be greater than 0"):
        swipe_utils.swipe_till_text_visibility("WhatsApp", Direction.DOWN, max_swipe=0)


@mark.unit_test
@patch("selenium.webdriver.common.action_chains.ActionChains.perform")
def test_long_swipe_down(mock_perform, swipe_utils, mock_driver):
    mock_driver.get_window_size.return_value = {"width": 1080, "height": 1920}
    swipe_utils.long_swipe(Direction.DOWN)
    mock_perform.assert_called_once()


@mark.unit_test
@patch("selenium.webdriver.common.action_chains.ActionChains.perform")
def test_long_swipe_up(mock_perform, swipe_utils, mock_driver):
    mock_driver.get_window_size.return_value = {"width": 1080, "height": 1920}
    swipe_utils.long_swipe(Direction.UP)
    mock_perform.assert_called_once()


@mark.unit_test
@patch("selenium.webdriver.common.action_chains.ActionChains.perform")
def test_short_swipe(mock_perform, swipe_utils, mock_driver):
    mock_driver.get_window_size.return_value = {"width": 1080, "height": 1920}
    swipe_utils.short_swipe(Direction.UP)
    mock_perform.assert_called_once()


@mark.unit_test
@patch("selenium.webdriver.common.action_chains.ActionChains.perform")
def test_swipe(mock_perform, swipe_utils, mock_driver):
    mock_driver.get_window_size.return_value = {"width": 1080, "height": 1920}
    swipe_utils.swipe(100, 200, 100, 800, iterate_times=3)
    assert mock_perform.call_count == 3
