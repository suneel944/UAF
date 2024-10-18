from typing import cast
from uaf.enums.mobile_os import MobileOs
from uaf.enums.appium_automation_name import AppiumAutomationName
from uaf.enums.browser_make import MobileWebBrowserMake


class Capabilities:
    """
    Web/Mobile Capabilities generation class
    """

    def __init__(self):
        self.__mobile_native_app_capabilities = {}
        self.__mobile_web_browser_capabilities = {}
        self.__mobile_hybrid_app_capabilities = {}

    @staticmethod
    def get_instance():
        """
        Retrieves Capabilities class instance
        """
        return Capabilities()

    def set_mobile_native_app_capabilities(self, **kwargs):
        """
        Sets mobile native app capabilities

        keyword arguments (kwargs):
        1.  platform_name\n
        2.  app_path\n
        3.  device_name\n
        4.  device_id\n
        5.  app_activity\n
        6.  app_package\n
        7.  auto_grant_permissions\n
        8.  automation_name\n
        9.  no_reset\n
        10. full_reset\n
        11. print_page_source_on_find_failure\n
        """
        if len(kwargs) < 1:
            raise ValueError("Missing keyword arguments!")

        self.__mobile_native_app_capabilities["platformName"] = cast(
            MobileOs, kwargs.get("platform_name")
        ).value
        self.__mobile_native_app_capabilities["app"] = kwargs.get("app_path")
        self.__mobile_native_app_capabilities["deviceName"] = kwargs.get("device_name")
        self.__mobile_native_app_capabilities["udid"] = kwargs.get("device_id")
        self.__mobile_native_app_capabilities["appActivity"] = kwargs.get(
            "app_activity"
        )
        self.__mobile_native_app_capabilities["appPackage"] = kwargs.get("app_package")
        self.__mobile_native_app_capabilities["autoGrantPermissions"] = cast(
            bool, kwargs.get("auto_grant_permissions")
        )
        self.__mobile_native_app_capabilities["automationName"] = cast(
            AppiumAutomationName, kwargs.get("automation_name")
        ).value
        self.__mobile_native_app_capabilities["noReset"] = kwargs.get("no_reset")
        self.__mobile_native_app_capabilities["fullReset"] = kwargs.get("full_reset")
        self.__mobile_native_app_capabilities["printPageSourceOnFindFailure"] = (
            kwargs.get("print_page_source_on_find_failure")
        )

    def set_mobile_web_browser_capabilities(self, **kwargs):
        """
        Sets mobile web browser capabilities

        keyword arguments (kwargs):
        1.  platform_name\n
        2.  device_name\n
        3.  device_id\n
        4.  auto_grant_permissions\n
        5.  automation_name\n
        6.  browser_name\n
        7.  no_reset\n
        8.  full_reset\n
        9.  print_page_source_on_find_failure\n
        """
        if len(kwargs) < 1:
            raise ValueError("Missing keyword arguments!")

        self.__mobile_web_browser_capabilities["platformName"] = cast(
            MobileOs, kwargs.get("platform_name")
        ).value
        self.__mobile_web_browser_capabilities["deviceName"] = kwargs.get("device_name")
        self.__mobile_web_browser_capabilities["udid"] = kwargs.get("device_id")
        self.__mobile_web_browser_capabilities["autoGrantPermissions"] = kwargs.get(
            "auto_grant_permissions"
        )
        self.__mobile_web_browser_capabilities["automationName"] = cast(
            AppiumAutomationName, kwargs.get("automation_name")
        ).value
        self.__mobile_web_browser_capabilities["browserName"] = cast(
            MobileWebBrowserMake, kwargs.get("browser_name")
        ).value
        self.__mobile_web_browser_capabilities["noReset"] = kwargs.get("no_reset")
        self.__mobile_web_browser_capabilities["fullReset"] = kwargs.get("full_reset")
        self.__mobile_web_browser_capabilities["printPageSourceOnFindFailure"] = (
            kwargs.get("print_page_source_on_find_failure")
        )

    def set_mobile_hybrid_app_capabilities(self, **kwargs):
        """
        Sets mobile hybrid app capabilities

        keyword arguments (kwargs):
        1.  platform_name\n
        2.  app_path\n
        3.  device_name\n
        4.  device_id\n
        5.  app_activity\n
        6.  app_package\n
        7.  auto_grant_permissions\n
        8.  automation_name\n
        9.  browser_name\n
        10. no_reset\n
        11. full_reset\n
        12. print_page_source_on_find_failure\n
        """
        if len(kwargs) < 1:
            raise ValueError("Missing keyword arguments!")

        self.__mobile_hybrid_app_capabilities["platformName"] = cast(
            MobileOs, kwargs.get("platform_name")
        ).value
        self.__mobile_hybrid_app_capabilities["app"] = kwargs.get("app_path")
        self.__mobile_hybrid_app_capabilities["deviceName"] = kwargs.get("device_name")
        self.__mobile_hybrid_app_capabilities["udid"] = kwargs.get("device_id")
        self.__mobile_hybrid_app_capabilities["appActivity"] = kwargs.get(
            "app_activity"
        )
        self.__mobile_hybrid_app_capabilities["appPackage"] = kwargs.get("app_package")
        self.__mobile_hybrid_app_capabilities["autoGrantPermissions"] = kwargs.get(
            "auto_grant_permissions"
        )
        self.__mobile_hybrid_app_capabilities["automationName"] = cast(
            AppiumAutomationName, kwargs.get("automation_name")
        ).value
        self.__mobile_hybrid_app_capabilities["browserName"] = cast(
            MobileWebBrowserMake, kwargs.get("browser_name")
        ).value
        self.__mobile_hybrid_app_capabilities["noReset"] = kwargs.get("no_reset")
        self.__mobile_hybrid_app_capabilities["fullReset"] = kwargs.get("full_reset")
        self.__mobile_hybrid_app_capabilities["printPageSourceOnFindFailure"] = (
            kwargs.get("print_page_source_on_find_failure")
        )

    def get_mobile_native_app_capabilities(self):
        """
        Retrieves the set mobile native app capabilities
        """
        return self.__mobile_native_app_capabilities

    def get_mobile_hybrid_app_capabilities(self):
        """
        Retrieves the set mobile hybrid app capabilities
        """
        return self.__mobile_hybrid_app_capabilities

    def get_mobile_web_browser_capabilities(self):
        """
        Retrieves the set mobile web browser capabilities
        """
        return self.__mobile_web_browser_capabilities
