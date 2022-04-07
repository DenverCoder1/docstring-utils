import inspect
import json
import sys
from types import FunctionType
from typing import Any, Dict, List

from docstring_utils import parse_docstring

from sample_code.google import *
from sample_code.numpy import *
from sample_code.sphinx import *


def _get_test_functions():
    """Returns a list of functions to test."""
    return [
        obj
        for _, obj in inspect.getmembers(sys.modules[__name__])
        if inspect.isfunction(obj)
    ]


def _format_failure_message(
    func: FunctionType,
    parsed_docstring: Dict[str, Any],
    expected_args: List[str],
    actual_args: List[str],
) -> str:
    """Formats a failure message for an argument test.

    Parameters
    ----------
    func: :class:`FunctionType`
        The function to parse the docstring of.
    parsed_docstring: :class:`Dict[str, Any]`
        The parsed docstring.
    expected_args: :class:`List[str]`
        The expected arguments.
    actual_args: :class:`List[str]`
        The actual arguments.

    Returns
    -------
    :class:`str`
        The failure message.
    """
    message = f"Expected {expected_args} but got {actual_args}"
    message = (
        f"{'=' * len(message)}\n"
        f"Testing {func.__name__}\n"
        f'"""{func.__doc__}"""\n'
        f"{json.dumps(parsed_docstring, indent=4)}\n"
        f"{'!' * len(message)}\n"
        f"{message}\n"
        f"{'!' * len(message)}\n"
    )
    return message


def test_parse_arguments():
    """Tests the parse_docstring function arguments list"""
    for func in _get_test_functions():
        parsed_docstring = parse_docstring(func)
        expected_args = [
            arg
            for arg in inspect.signature(func).parameters.keys()
            if arg not in ("self", "cls")
        ]
        actual_args = list(parsed_docstring["args"].keys())
        message = _format_failure_message(
            func, parsed_docstring, expected_args, actual_args
        )
        assert expected_args == actual_args, message


def test_parse_arguments_filter():
    """Tests the parse_docstring function arguments list with filtering"""
    for func in _get_test_functions():
        parsed_docstring = parse_docstring(func, filter_args=True)
        expected_args = [
            arg
            for arg in inspect.signature(func).parameters.keys()
            if arg not in ("self", "cls")
        ]
        actual_args = list(parsed_docstring["args"].keys())
        message = _format_failure_message(
            func, parsed_docstring, expected_args, actual_args
        )
        assert expected_args == actual_args, message
