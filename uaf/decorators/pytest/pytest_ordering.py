def order(n):
    """
    This decorator marks a test function with a specified order
    """

    def decorator(func):
        setattr(func, "_order", n)
        return func

    return decorator


def pytest_collection_modifyitems(items):
    """
    This hook is called after collecting all the test items and allows modifying the test item list
    """
    items.sort(key=lambda item: item.obj._order if hasattr(item.obj, "_order") else float("inf"))
