def google_short_description():
    """Example of a Google-style docstring."""
    pass


def google_extended_description():
    """Example of a Google-style docstring.

    This is a longer description of what the function or class does. It may
    span multiple lines.
    """
    pass


def google_argument(arg1):
    """Example of a Google-style docstring.

    Args:
        arg1: Description of `arg1`.
    """
    pass


def google_arguments(arg1, arg2):
    """Example of a Google-style docstring.

    Args:
        arg1: Description of `arg1`.
        arg2: Description of `arg2`.
    """
    pass


def google_arguments_with_types(arg1: str, arg2: int):
    """Example of a Google-style docstring.

    Args:
        arg1 (str): Description of `arg1`.
        arg2 (int): Description of `arg2`.
    """
    pass


def google_return_value(arg1: str, arg2) -> int:
    """Example of a Google-style docstring.

    Args:
        arg1 (str): Description of `arg1`.
        arg2: Description of `arg2`.

    Returns:
        int: Description of `return` value.
    """
    return 0


def google_other_parameters(arg1: str, arg2) -> int:
    """Example of a Google-style docstring.

    Parameters:
        arg1 (str): Description of `arg1`.

    Other Parameters:
        arg2: Description of `arg2`.

    Returns:
        int: Description of `return` value.
    """
    return 0


def google_multiline_descriptions(arg1, arg2):
    """Example of a Google-style docstring.

    This is a longer description of what the function or class does. It may
    span multiple lines.

    Args:
        arg1 (str): Description of `arg1`.
            This is an extended description of `arg1`. It can also span multiple
            lines.
        arg2 (int): Description of `arg2`.

            This is also part of `arg2`. There can be empty lines.
    """
    pass
