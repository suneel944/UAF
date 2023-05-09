from uaf.decorators.loggers.logger import log
from uaf.utilities.selenium.waiter.waits import Waits


class WindowUtils:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = Waits(driver)

    @log
    def switch_to_succeeding_window(self):
        handle_pointer = ""
        handle = self.driver.current_window_handle
        window_handles: list[str] = self.driver.window_handles
        window_handles_size = len(window_handles)
        for i in range(window_handles_size):
            handle_pointer = window_handles[i]
            if handle_pointer.__eq__(handle):
                if i == (window_handles_size - 1):
                    handle_pointer = window_handles[i]
                    break
                handle_pointer = window_handles[i + 1]
                break
        # switch to window
        self.driver.switch_to.window(handle_pointer)

    @log
    def switch_to_preceeding_window(self):
        handle_pointer = ""
        handle = self.driver.current_window_handle
        window_handles: list[str] = self.driver.window_handles
        window_handles_size = len(window_handles)
        for i in range(window_handles_size):
            handle_pointer = window_handles[i]
            if handle_pointer.__eq__(handle):
                if i == 0:
                    handle_pointer = window_handles[window_handles_size - 1]
                    break
                handle_pointer = window_handles[i - 1]
                break
        # switch to window
        self.driver.switch_to.window(handle)

    @log
    def switch_to_tab(self, tab_index: int):
        window_handles: list[str] = self.driver.window_handles
        self.driver.switch_to_window(window_handles[tab_index])
