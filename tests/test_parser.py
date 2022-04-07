from typing import Any, Dict

from docstring_utils import parse_docstring

from test_helper import format_failure_message, get_test_functions


def test_parse_arguments():
    """Tests the parse_docstring function arguments list"""
    for func in get_test_functions():
        parsed_docstring = parse_docstring(func)
        expected_docstring: Dict[str, Any] = func()
        message = format_failure_message(
            func, parsed_docstring, expected_docstring, parsed_docstring
        )
        assert expected_docstring == parsed_docstring, message


def test_parse_arguments_filter():
    """Tests the parse_docstring function arguments list with filtering"""
    for func in get_test_functions():
        parsed_docstring = parse_docstring(func, filter_args=True)
        expected_docstring: Dict[str, Any] = func()
        message = format_failure_message(
            func, parsed_docstring, expected_docstring, parsed_docstring
        )
        assert expected_docstring == parsed_docstring, message
