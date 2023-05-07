import io
import os

from setuptools import setup

with io.open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def library_version():
    # Define the logic to retrieve the library version
    # Replace this with your actual implementation
    return "1.0.0"


setup(
    name="uaf",
    version=library_version(),
    description="Universal automation framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "uaf",
        "uaf python",
        "api automation",
        "web automation",
        "mobile automation",
    ],
    # Rest of the setup configuration...
)
