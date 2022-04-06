def numpy_short_description():
    """Example of a Numpy-style docstring."""
    pass


def numpy_extended_description():
    """Example of a Numpy-style docstring.

    This is a longer description of what the function or class does. It may
    span multiple lines.
    """
    pass


def numpy_argument(arg1):
    """Example of a Numpy-style docstring.

    Parameters
    ----------
    arg1
        Description of `arg1`.
    """
    pass


def numpy_arguments(arg1, arg2):
    """Example of a Numpy-style docstring.

    Parameters
    ----------
    arg1
        Description of `arg1`.
    arg2
        Description of `arg2`.
    """
    pass


def numpy_arguments_with_types(arg1: str, arg2: int):
    """Example of a Numpy-style docstring.

    Parameters
    ----------
    arg1 : str
        Description of `arg1`.
    arg2 : int
        Description of `arg2`.
    """
    pass


def numpy_return_value(arg1: str) -> int:
    """Example of a Numpy-style docstring.

    Parameters
    ----------
    arg1 : str
        Description of `arg1`.

    Returns
    -------
    int
        Description of `return` value.
    """
    return 0


def numpy_other_parameters(arg1: str, arg2) -> int:
    """Example of a Numpy-style docstring.

    Arguments
    ---------
    arg1 : str
        Description of `arg1`.

    Other Parameters
    ----------------
    arg2
        Description of `arg2`.

    Returns
    -------
    int
        Description of `return` value.
    """
    return 0


def numpy_multiline_descriptions(arg1, arg2):
    """Example of a Numpy-style docstring.

    Parameters
    ----------
    arg1
        Description of `arg1`.
        This is an extended description. It can span multiple lines.
    arg2
        Description of `arg2`.

        This is an extended description. It can have empty lines.
    """
    pass
