def short_description():
    """Example of a Sphinx-style docstring."""
    pass


def extended_description():
    """Example of a Sphinx-style docstring.

    This is a longer description of what the function or class does. It may
    span multiple lines.
    """
    pass


def arguments(arg1):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    """
    pass


def arguments_with_types(arg1: str, arg2: int):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    :type arg1: :class:`str`
    :param arg2: Description of `arg2`.
    :type arg2: :class:`int`
    """
    pass


def return_value(arg1: str) -> int:
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    :type arg1: :class:`str`
    :return: Description of `return` value.
    :rtype: :class:`int`
    """
    return 0
