def sample_numpy_short_description():
    """Example of a Numpy-style docstring."""
    return {
        "description": "Example of a Numpy-style docstring.",
        "args": {},
        "return": {"type": "", "description": ""},
    }


def sample_numpy_extended_description():
    """Example of a Numpy-style docstring.

    This is a longer description of what the function or class does. It may
    span multiple lines.
    """
    return {
        "description": "Example of a Numpy-style docstring.",
        "args": {},
        "return": {"type": "", "description": ""},
    }


def sample_numpy_argument(arg1=None):
    """Example of a Numpy-style docstring.

    Parameters
    ----------
    arg1
        Description of `arg1`.
    """
    return {
        "description": "Example of a Numpy-style docstring.",
        "args": {"arg1": {"description": "Description of `arg1`.", "type": ""}},
        "return": {"type": "", "description": ""},
    }


def sample_numpy_arguments(arg1=None, arg2=None):
    """Example of a Numpy-style docstring.

    Parameters
    ----------
    arg1
        Description of `arg1`.
    arg2
        Description of `arg2`.
    """
    return {
        "description": "Example of a Numpy-style docstring.",
        "args": {
            "arg1": {"description": "Description of `arg1`.", "type": ""},
            "arg2": {"description": "Description of `arg2`.", "type": ""},
        },
        "return": {"type": "", "description": ""},
    }


def sample_numpy_arguments_with_types(arg1=None, arg2=None):
    """Example of a Numpy-style docstring.

    Parameters
    ----------
    arg1: str
        Description of `arg1`.
    arg2 : int
        Description of `arg2`.
    """
    return {
        "description": "Example of a Numpy-style docstring.",
        "args": {
            "arg1": {"description": "Description of `arg1`.", "type": "str"},
            "arg2": {"description": "Description of `arg2`.", "type": "int"},
        },
        "return": {"type": "", "description": ""},
    }


def sample_numpy_return_value(arg1=None):
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
    return {
        "description": "Example of a Numpy-style docstring.",
        "args": {"arg1": {"description": "Description of `arg1`.", "type": "str"}},
        "return": {"description": "Description of `return` value.", "type": "int"},
    }


def sample_numpy_other_parameters(arg1=None, arg2=None):
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
    return {
        "description": "Example of a Numpy-style docstring.",
        "args": {
            "arg1": {"description": "Description of `arg1`.", "type": "str"},
            "arg2": {"description": "Description of `arg2`.", "type": ""},
        },
        "return": {"description": "Description of `return` value.", "type": "int"},
    }


def sample_numpy_multiline_descriptions(arg1=None, arg2=None):
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
    return {
        "description": "Example of a Numpy-style docstring.",
        "args": {
            "arg1": {
                "description": "Description of `arg1`. This is an extended description. It can span multiple lines.",
                "type": "",
            },
            "arg2": {"description": "Description of `arg2`.", "type": ""},
        },
        "return": {"type": "", "description": ""},
    }
