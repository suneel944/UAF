from pytest import mark

from tests.fixtures.conftest import web_driver  # type: ignore
from uaf.enums.browser_make import WebBrowserMake


@mark.skip(reason="skipping as it requires manual set up of infra")
@mark.unit_test
@mark.parametrize(
    "web_driver",
    [
        {"arg_browser_make": WebBrowserMake.CHROME},
        {"arg_browser_make": WebBrowserMake.BRAVE},
        {"arg_browser_make": WebBrowserMake.FIREFOX},
        {"arg_browser_make": WebBrowserMake.MSEDGE},
    ],
    indirect=True,
)
def test_web_driver_factory(web_driver):
    web_driver.get("https://www.google.co.in/")
    title = web_driver.title
    assert isinstance(title, str) and title.lower().__eq__("google")
