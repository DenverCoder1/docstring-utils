def sphinx_short_description():
    """Example of a Sphinx-style docstring."""
    pass


def sphinx_extended_description():
    """Example of a Sphinx-style docstring.

    This is a longer description of what the function or class does. It may
    span multiple lines.
    """
    pass


def sphinx_argument(arg1):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    """
    pass


def sphinx_arguments(arg1, arg2):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    :param arg2: Description of `arg2`.
    """
    pass


def sphinx_arguments_with_types(arg1: str, arg2: int):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    :type arg1: :class:`str`
    :param arg2: Description of `arg2`.
    :type arg2: :class:`int`
    """
    pass


def sphinx_return_value(arg1: str) -> int:
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    :type arg1: :class:`str`
    :return: Description of `return` value.
    :rtype: :class:`int`
    """
    return 0


def sphinx_multiline_descriptions(arg1: str, arg2):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
        This is a multi-line description.
    :type arg1: :class:`str`
    :param arg2: Description of `arg2`.

        This is a multi-line description. There can be blank lines.
    """
    pass
