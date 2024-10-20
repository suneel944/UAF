from pytest import mark

from uaf.common.helper import library_version
from uaf import version as uaf_version


@mark.unit_test
def test_library_version():
    assert library_version() == uaf_version.version
    assert isinstance(library_version(), str)
