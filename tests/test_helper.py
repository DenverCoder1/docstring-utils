import inspect
import json
import sys
from typing import Any, Callable, Dict

from sample_code.google import *
from sample_code.numpy import *
from sample_code.sphinx import *


def get_test_functions():
    """Returns a list of functions to test."""
    return [
        obj
        for _, obj in inspect.getmembers(sys.modules[__name__])
        if (inspect.isfunction(obj) and obj.__name__.startswith("sample_"))
    ]


def format_failure_message(
    func: Callable[..., Any],
    parsed_docstring: Dict[str, Any],
    expected: Any,
    actual: Any,
) -> str:
    """Formats a failure message for an argument test.

    Parameters
    ----------
    func: :class:`FunctionType`
        The function to parse the docstring of.
    parsed_docstring: :class:`Dict[str, Any]`
        The parsed docstring.
    expected: Any
        The expected
    actual: Any
        The actual return description.

    Returns
    -------
    :class:`str`
        The failure message.
    """
    MAX_SEPERATOR_WIDTH = 100
    message = f'Expected "{expected}" but got "{actual}"'
    message = (
        f"{'=' * min(MAX_SEPERATOR_WIDTH, len(message))}\n"
        f"Testing {func.__name__}\n"
        f'"""{func.__doc__}"""\n'
        f"{json.dumps(parsed_docstring, indent=4)}\n"
        f"{'!' * min(MAX_SEPERATOR_WIDTH, len(message))}\n"
        f"{message}\n"
        f"{'!' * min(MAX_SEPERATOR_WIDTH, len(message))}\n"
    )
    return message
