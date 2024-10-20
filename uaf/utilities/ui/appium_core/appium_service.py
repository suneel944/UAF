import os
import subprocess
import time
import requests
import shutil


class AppiumServiceError(Exception):
    """Custom exception raised when there is an error with the Appium service."""

    pass


class AppiumService:
    """A custom Appium service launcher that simplifies starting and stopping Appium."""

    def __init__(self):
        """Initializes the AppiumService instance with process and command placeholders."""
        self.process: subprocess.Popen[bytes] | None = None
        self.cmd: list[str] | None = None

    def start(
        self,
        args: list[str] | None = None,
        stdout: int | None = subprocess.PIPE,
        stderr: int | None = subprocess.PIPE,
        env: dict[str, str] | None = None,
        timeout: int = 60,
    ) -> None:
        """
        Starts the Appium service with the specified arguments.

        Args:
            args (list[str] | None): Arguments to pass to the Appium server. Defaults to None.
            stdout (int | None): Standard output configuration for the subprocess. Defaults to subprocess.PIPE.
            stderr (int | None): Standard error configuration for the subprocess. Defaults to subprocess.PIPE.
            env (dict[str, str] | None): Environment variables for the subprocess. Defaults to None.
            timeout (int): Maximum time in seconds to wait for the server to start. Defaults to 60 seconds.

        Raises:
            AppiumServiceError: If the Appium executable is not found or the service fails to start.
        """
        self.stop()
        appium_executable = shutil.which("appium")
        if not appium_executable:
            raise AppiumServiceError(
                "Appium executable not found. Ensure Appium is installed and available in your PATH."
            )

        self.cmd = [appium_executable]
        if args:
            self.cmd.extend(args)

        # Start the Appium server process
        self.process = subprocess.Popen(
            self.cmd,
            stdout=stdout,
            stderr=stderr,
            env=env or os.environ.copy(),
        )

        # Wait for the server to start
        start_time = time.time()
        status_url = self._get_status_url(args)
        while time.time() - start_time < timeout:
            if self.process.poll() is not None:
                # Process has exited prematurely
                stderr_output = (
                    self.process.stderr.read().decode("utf-8")
                    if self.process.stderr
                    else ""
                )
                raise AppiumServiceError(
                    f"Appium server process exited prematurely.\nStderr: {stderr_output}"
                )
            try:
                response = requests.get(status_url, timeout=1)
                if response.status_code == 200:
                    # Server is up and running
                    return
            except requests.exceptions.ConnectionError:
                pass
            time.sleep(1)

        # Timeout exceeded without server start
        self.stop()
        raise AppiumServiceError(
            f"Appium server did not start within {timeout} seconds."
        )

    def _get_status_url(self, args: list[str] | None) -> str:
        """
        Constructs the status URL for checking the Appium server's status.

        Args:
            args (list[str] | None): List of arguments passed to the Appium server.

        Returns:
            str: The status URL used to check if the server is running.
        """
        host = "127.0.0.1"
        port = "4723"
        base_path = "/"
        if args:
            for i in range(len(args)):
                if args[i] in ("--address", "-a") and i + 1 < len(args):
                    host = args[i + 1]
                elif args[i] in ("--port", "-p") and i + 1 < len(args):
                    port = args[i + 1]
                elif args[i] in ("--base-path", "-pa") and i + 1 < len(args):
                    base_path = args[i + 1]
        base_path = base_path.rstrip("/") + "/"
        return f"http://{host}:{port}{base_path}status"

    def stop(self) -> None:
        """
        Stops the Appium service if it is running.

        Terminates the process and waits for it to stop, forcibly killing it if necessary.
        """
        if self.process:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
            self.process = None
            self.cmd = None

    @property
    def is_running(self) -> bool:
        """
        Checks if the Appium service is currently running.

        Returns:
            bool: True if the service is running, False otherwise.
        """
        return self.process is not None and self.process.poll() is None

    def __enter__(self) -> "AppiumService":
        """
        Enters the runtime context for the AppiumService.

        Returns:
            AppiumService: The service instance.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        Exits the runtime context and stops the Appium service.

        Ensures that the service is properly terminated when exiting the context.
        """
        self.stop()
