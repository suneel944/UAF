import io
import os

from setuptools import find_packages, setup

from uaf.common.helper import library_version

setup(
    name="uaf",
    version=library_version(),
    description="Universal automation framework",
    long_description=open(
        os.path.join(os.path.dirname("__file__"), "README.md"), encoding="utf-8"
    ).read(),
    keywords=[
        "uaf",
        "uaf python",
        "api automation",
        "web automation",
        "mobile automation",
    ],
    author="Suneel Kaushik Subramanya",
    author_email="suneel944@gmail.com",
    maintainer="Suneel Kaushik Subramanya",
    package_data={"uaf": ["py.typed"]},
    packages=find_packages(include=["uaf*"]),
    license="MIT",
    # A list of classifiers to help users find your package on PyPI
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
    ],
)
