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
        Retrives Capabilities class instance
        """
        return Capabilities()

    def set_mobile_native_app_capabilities(self, **kwargs):
        """
        Sets mobile native app capabilities

        keyword arguments (kwargs):
        1.  platform_name\n
        2.  app_path\n
        3.  device_name\ns
        4.  device_id\n
        5.  app_activity\n
        6.  app_package\n
        7.  auto_grant_permissions\n
        8.  automation_name\n
        """
        if kwargs.__len__() < 1:
            raise ValueError("Missing keyword arguments!")
        self.__mobile_native_app_capabilities["platformName"] = kwargs.get("platform_name").value  # type: ignore
        self.__mobile_native_app_capabilities["app"] = kwargs.get("app_path")  # type: ignore
        self.__mobile_native_app_capabilities["deviceName"] = kwargs.get("device_name")  # type: ignore
        self.__mobile_native_app_capabilities["udid"] = kwargs.get("device_id")  # type: ignore
        self.__mobile_native_app_capabilities["appActivity"] = kwargs.get("app_activity")  # type: ignore
        self.__mobile_native_app_capabilities["appPackage"] = kwargs.get("app_package")  # type: ignore
        self.__mobile_native_app_capabilities["autoGrantPermissions"] = kwargs.get(
            "auto_grant_permissions"
        )
        self.__mobile_native_app_capabilities["automationName"] = kwargs.get("automation_name").value  # type: ignore

    def set_mobile_web_browser_capabilities(self, **kwargs):
        """
        Sets mobile web browser capabilities

        keyword arguments (kwargs):
        1.  platform_name\n
        2.  device_name\n
        3.  device_id\n
        4.  auto_grant permissions\n
        5.  automation_name\n
        6.  browser_name\n
        """
        if kwargs.__len__() < 1:
            raise ValueError("Missing keyword arguments!")
        self.__mobile_web_browser_capabilities["platformName"] = kwargs.get("platform_name").value  # type: ignore
        self.__mobile_web_browser_capabilities["deviceName"] = kwargs.get("device_name")
        self.__mobile_web_browser_capabilities["udid"] = kwargs.get("device_id")
        self.__mobile_web_browser_capabilities["autoGrantPermissions"] = kwargs.get(
            "auto_grant_permissions"
        )
        self.__mobile_web_browser_capabilities["automationName"] = kwargs.get("automation_name").value  # type: ignore
        self.__mobile_web_browser_capabilities["browserName"] = kwargs.get("browser_name").value  # type: ignore

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
        """
        if kwargs.__len__() < 1:
            raise ValueError("Missing keyword arguments!")
        self.__mobile_hybrid_app_capabilities["platformName"] = kwargs.get("platform_name").value  # type: ignore
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
        self.__mobile_hybrid_app_capabilities["automationName"] = kwargs.get("automation_name").value  # type: ignore
        self.__mobile_hybrid_app_capabilities["browserName"] = kwargs.get("browser_name").value  # type: ignore

    def get_mobile_native_app_capabilities(self):
        return self.__mobile_native_app_capabilities

    def get_mobile_hybrid_app_capabilities(self):
        return self.__mobile_hybrid_app_capabilities

    def get_mobile_web_browser_capabilities(self):
        return self.__mobile_web_browser_capabilities
