from . import Enum


class TestEnvironments(Enum):
    DEVELOPMENT = "dev"
    STAGE = "stage"
    QA = "qa"
    PRODUCTION = "prod"
