import inspect
import json
import sys

from docstring_utils import parse_docstring

from sample_code.google import *
from sample_code.numpy import *
from sample_code.sphinx import *


def _get_test_functions():
    return [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if (
            inspect.isfunction(obj)
            and name not in (
                "parse_docstring",
                "test_parse_docstrings",
                "test_parse_docstrings_filter",
                "_get_test_functions",
                "_format_failure_message",
            )
        )
    ]


def _format_failure_message(func, parsed_docstring, expected_args, actual_args):
    message = f"Arguments {expected_args} do not match {actual_args}"
    message = (
        "=" * len(message)
        + "\n"
        + f"Testing {func.__name__}\n"
        + f'"""{func.__doc__}"""\n'
        + f"{json.dumps(parsed_docstring, indent=4)}\n"
        + "!" * len(message)
        + "\n"
        + message
        + "\n"
        + "!" * len(message)
        + "\n"
    )
    print(message)
    return message


def test_parse_docstrings():
    for func in _get_test_functions():
        parsed_docstring = parse_docstring(func)
        actual_args = [
            arg
            for arg in inspect.signature(func).parameters.keys()
            if arg not in ("self", "cls")
        ]
        expected_args = list(parsed_docstring["args"].keys())
        message = _format_failure_message(func, parsed_docstring, expected_args, actual_args)
        assert actual_args == expected_args, message


def test_parse_docstrings_filter():
    for func in _get_test_functions():
        parsed_docstring = parse_docstring(func, filter_args=True)
        actual_args = [
            arg
            for arg in inspect.signature(func).parameters.keys()
            if arg not in ("self", "cls")
        ]
        expected_args = list(parsed_docstring["args"].keys())
        message = _format_failure_message(func, parsed_docstring, expected_args, actual_args)
        assert actual_args == expected_args, message
