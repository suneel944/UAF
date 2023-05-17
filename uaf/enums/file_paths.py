from . import Enum, unique


@unique
class FilePaths(Enum):
    """File Paths as constants

    Args:
        Enum (FilePaths): enum
    """

    COMMON = "configs/test/common.yml"
    TEST_CONFIG_DEV = "configs/test/environments/dev.yml"
    TEST_CONFIG_QA = "configs/test/environments/qa.yml"
    TEST_CONFIG_STAGE = "configs/test/environments/stage.yml"
    TEST_CONFIG_PROD = "configs/test/environments/prod.yml"
