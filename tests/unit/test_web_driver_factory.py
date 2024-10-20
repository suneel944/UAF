from typing import cast
import pytest
from pytest import mark
from unittest.mock import MagicMock, patch
from uaf.enums.browser_make import WebBrowserMake
from uaf.factories.driver.concrete_factory.concrete_factory import (
    ConcreteWebDriverFactory,
)


@pytest.fixture
def mock_web_driver():
    return MagicMock()


@mark.unit_test
@mark.parametrize(
    "browser_make",
    [
        (WebBrowserMake.CHROME),
        (WebBrowserMake.BRAVE),
        (WebBrowserMake.FIREFOX),
        (WebBrowserMake.MSEDGE),
    ],
)
def test_web_driver_factory_valid_browsers(mock_web_driver, browser_make):
    with patch(
        "uaf.factories.driver.concrete_factory.concrete_products.web.concrete_web_driver.ConcreteWebDriver.get_web_driver",
        return_value=mock_web_driver,
    ) as MockGetWebDriver:
        factory = ConcreteWebDriverFactory()
        driver = factory.get_web_driver(browser_make=browser_make)
        MockGetWebDriver.assert_called_once()
        assert driver == mock_web_driver


@mark.unit_test
def test_web_driver_factory_invalid_browser():
    factory = ConcreteWebDriverFactory()
    invalid_browser = cast(WebBrowserMake, "invalid_browser")

    with pytest.raises(
        ValueError, match="Invalid browser type specified: invalid_browser"
    ):
        factory.get_web_driver(browser_make=invalid_browser)


@mark.unit_test
def test_web_driver_factory_none_browser():
    factory = ConcreteWebDriverFactory()
    none_browser = cast(WebBrowserMake, None)

    with pytest.raises(ValueError, match="Invalid browser type specified: None"):
        factory.get_web_driver(browser_make=none_browser)


@mark.unit_test
@mark.parametrize(
    "browser_make",
    [
        (WebBrowserMake.CHROME),
        (WebBrowserMake.BRAVE),
        (WebBrowserMake.FIREFOX),
        (WebBrowserMake.MSEDGE),
    ],
)
def test_web_driver_factory_with_options(mock_web_driver, browser_make):
    custom_options = {"start-maximized": True}

    with patch(
        "uaf.factories.driver.concrete_factory.concrete_products.web.concrete_web_driver.ConcreteWebDriver.get_web_driver",
        return_value=mock_web_driver,
    ) as MockGetWebDriver:
        factory = ConcreteWebDriverFactory()
        driver = factory.get_web_driver(
            browser_make=browser_make, options=custom_options
        )
        MockGetWebDriver.assert_called_once_with(options=custom_options)
        assert driver == mock_web_driver


@mark.unit_test
@mark.parametrize(
    "browser_make",
    [
        (WebBrowserMake.CHROME),
        (WebBrowserMake.BRAVE),
        (WebBrowserMake.FIREFOX),
        (WebBrowserMake.MSEDGE),
    ],
)
def test_web_driver_factory_without_options(mock_web_driver, browser_make):
    with patch(
        "uaf.factories.driver.concrete_factory.concrete_products.web.concrete_web_driver.ConcreteWebDriver.get_web_driver",
        return_value=mock_web_driver,
    ) as MockGetWebDriver:
        factory = ConcreteWebDriverFactory()
        driver = factory.get_web_driver(browser_make=browser_make)
        MockGetWebDriver.assert_called_once_with(options=None)
        assert driver == mock_web_driver


@mark.unit_test
@mark.parametrize(
    "browser_make",
    [
        (WebBrowserMake.CHROME),
        (WebBrowserMake.BRAVE),
        (WebBrowserMake.FIREFOX),
        (WebBrowserMake.MSEDGE),
    ],
)
def test_web_driver_factory_multiple_calls(mock_web_driver, browser_make):
    with patch(
        "uaf.factories.driver.concrete_factory.concrete_products.web.concrete_web_driver.ConcreteWebDriver.get_web_driver",
        return_value=mock_web_driver,
    ) as MockGetWebDriver:
        factory = ConcreteWebDriverFactory()
        driver1 = factory.get_web_driver(browser_make=browser_make)
        MockGetWebDriver.assert_called_once()
        assert driver1 == mock_web_driver
        MockGetWebDriver.reset_mock()
        driver2 = factory.get_web_driver(browser_make=browser_make)
        MockGetWebDriver.assert_called_once()
        assert driver2 == mock_web_driver


@mark.unit_test
@mark.parametrize(
    "browser_make,extra_options",
    [
        (WebBrowserMake.CHROME, {"headless": True, "disable-gpu": True}),
        (WebBrowserMake.BRAVE, {"incognito": True}),
        (WebBrowserMake.FIREFOX, {"private-browsing": True}),
        (WebBrowserMake.MSEDGE, {"edge-option": "some-value"}),
    ],
)
def test_web_driver_factory_with_extra_options(
    mock_web_driver, browser_make, extra_options
):
    with patch(
        "uaf.factories.driver.concrete_factory.concrete_products.web.concrete_web_driver.ConcreteWebDriver.get_web_driver",
        return_value=mock_web_driver,
    ) as MockGetWebDriver:
        factory = ConcreteWebDriverFactory()
        driver = factory.get_web_driver(
            browser_make=browser_make, options=extra_options
        )
        MockGetWebDriver.assert_called_once_with(options=extra_options)
        assert driver == mock_web_driver
