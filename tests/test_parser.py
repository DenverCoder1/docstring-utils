from docstring_utils import parse_docstring

from test_helper import format_failure_message, get_test_functions


def test_parse_arguments():
    """Tests the parse_docstring function arguments list"""
    for func in get_test_functions():
        expected = func()
        actual = parse_docstring(func)._parsed_docstring  # type: ignore
        message = format_failure_message(func, expected, actual)
        assert expected == actual, message


def test_parse_arguments_filter():
    """Tests the parse_docstring function arguments list with filtering"""
    for func in get_test_functions():
        expected = func()
        actual = parse_docstring(func, filter_args=True)._parsed_docstring  # type: ignore
        message = format_failure_message(func, expected, actual)
        assert expected == actual, message
