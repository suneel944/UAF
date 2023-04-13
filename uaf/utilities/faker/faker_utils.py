from . import Any, Faker, Optional, random


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
        """Constructor

        Args:
            locale (str, optional): geographical style of names to utilise in generating fake data. Defaults to "en_US".
        """
        self.fake = Faker(locale)

    def random_int(self, min_val: int = 0, max_val: int = 100):
        """Generate random integer

        Args:
            min_val (int, optional): minimum value. Defaults to 0.
            max_val (int, optional): maximum value. Defaults to 100.

        Returns:
            int: random integer in specified range
        """
        return self.fake.random_int(min=min_val, max=max_val)

    def random_float(self, min_val: float = 0, max_val: float = 100):
        """Generate random floating point number

        Args:
            min_val (float, optional): minimum value. Defaults to 0.
            max_val (float, optional): maximum value. Defaults to 100.

        Returns:
            float: floating point number in specified range
        """
        return self.fake.pyfloat(min_value=min_val, max_value=max_val)

    def random_bool(self):
        """Returns random boolean condition, either True/False

        Returns:
            bool: True/False
        """
        return self.fake.pybool()

    def random_str(self, length: int, allowed_chars: Optional[str] = None):
        """Generate random string using in the allowed chars and specified length

        Args:
            length (int): length of the string
            allowed_chars (Optional[str], optional): string data. Defaults to None.
        """
        if allowed_chars:
            return "".join(random.choices(allowed_chars, k=length))
        return self.fake.pystr(min_chars=length, max_chars=length)

    def random_list(self, length: int = 10, item_type: Any = int, **kwargs):
        """Generates random list of data of same data type

        Args:
            length (int, optional): length of data. Defaults to 10.
            item_type (Any, optional): type of data. Defaults to int.

        Raises:
            ValueError: if provided unsupported data type

        Returns:
            list[Any]: list of data of same/specified data type
        """
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
