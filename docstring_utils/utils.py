from typing import Callable, Iterable, Optional, TypeVar

T = TypeVar("T")


def find(func: Callable[..., bool], iterable: Iterable[T]) -> Optional[T]:
    """Finds the first element in `iterable` for which `func` returns `True`.

    Parameters
    ----------
    func: Callable[..., bool]
        The function to test each element of `iterable` against.
    iterable: Iterable[Any]
        The iterable to test each element of.

    Returns
    -------
    Any
        The first element in `iterable` for which `func` returns `True` or
        None if no such element exists.
    """
    for element in iterable:
        if func(element):
            return element
    return None
