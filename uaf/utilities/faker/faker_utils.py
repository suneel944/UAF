from . import Faker, random, Optional, Any


class FakerUtils:
    """
    Utility class to generate fake data using Faker library
    """

    @staticmethod
    def get_instance():
        """
        Provides default instance with locale set en_US
        """
        return FakerUtils()

    def __init__(self, locale: str = "en_US"):
        self.fake = Faker(locale)

    def random_int(self, min_val: int = 0, max_val: int = 100):
        return self.fake.random_int(min=min_val, max=max_val)

    def random_float(self, min_val: float = 0, max_val: float = 100):
        return self.fake.pyfloat(min_value=min_val, max_value=max_val)

    def random_bool(self):
        return self.fake.pybool()

    def random_str(self, length: int, allowed_chars: Optional[str] = None):
        if allowed_chars:
            return "".join(random.choices(allowed_chars, k=length))
        return self.fake.pystr(min_chars=length, max_chars=length)

    def random_list(self, length: int = 10, item_type: Any = int, **kwargs):
        if isinstance(item_type, int):
            return [self.random_int(**kwargs) for _ in range(length)]
        elif isinstance(item_type, float):
            return [self.random_float(**kwargs) for _ in range(length)]
        elif isinstance(item_type, bool):
            return [self.random_bool(**kwargs) for _ in range(length)]
        elif isinstance(item_type, str):
            return [self.random_str(**kwargs) for _ in range(length)]
        else:
            raise ValueError(f"Unsupported item_type: {item_type}")
