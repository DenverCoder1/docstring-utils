def sample_google_short_description():
    """Example of a Google-style docstring."""
    return {
        "description": "Example of a Google-style docstring.",
        "args": {},
        "return": {"type": "", "description": ""},
    }


def sample_google_extended_description():
    """Example of a Google-style docstring.

    This is a longer description of what the function or class does. It may
    span multiple lines.
    """
    return {
        "description": "Example of a Google-style docstring.",
        "args": {},
        "return": {"type": "", "description": ""},
    }


def sample_google_argument(arg1=None):
    """Example of a Google-style docstring.

    Args:
        arg1: Description of `arg1`.
    """
    return {
        "description": "Example of a Google-style docstring.",
        "args": {"arg1": {"description": "Description of `arg1`.", "type": ""}},
        "return": {"type": "", "description": ""},
    }


def sample_google_arguments(arg1=None, arg2=None):
    """Example of a Google-style docstring.

    Args:
        arg1: Description of `arg1`.
        arg2: Description of `arg2`.
    """
    return {
        "description": "Example of a Google-style docstring.",
        "args": {
            "arg1": {"description": "Description of `arg1`.", "type": ""},
            "arg2": {"description": "Description of `arg2`.", "type": ""},
        },
        "return": {"type": "", "description": ""},
    }


def sample_google_arguments_with_types(arg1=None, arg2=None):
    """Example of a Google-style docstring.

    Args:
        arg1 (str): Description of `arg1`.
        arg2 (int): Description of `arg2`.
    """
    return {
        "description": "Example of a Google-style docstring.",
        "args": {
            "arg1": {"description": "Description of `arg1`.", "type": "str"},
            "arg2": {"description": "Description of `arg2`.", "type": "int"},
        },
        "return": {"type": "", "description": ""},
    }


def sample_google_return_value(arg1=None, arg2=None):
    """Example of a Google-style docstring.

    Args:
        arg1 (str): Description of `arg1`.
        arg2: Description of `arg2`.

    Returns:
        int: Description of `return` value.
    """
    return {
        "description": "Example of a Google-style docstring.",
        "args": {
            "arg1": {"description": "Description of `arg1`.", "type": "str"},
            "arg2": {"description": "Description of `arg2`.", "type": ""},
        },
        "return": {"description": "Description of `return` value.", "type": "int"},
    }


def sample_google_other_parameters(arg1=None, arg2=None):
    """Example of a Google-style docstring.

    Parameters:
        arg1 (str): Description of `arg1`.

    Other Parameters:
        arg2: Description of `arg2`.

    Returns:
        int: Description of `return` value.
    """
    return {
        "description": "Example of a Google-style docstring.",
        "args": {
            "arg1": {"description": "Description of `arg1`.", "type": "str"},
            "arg2": {"description": "Description of `arg2`.", "type": ""},
        },
        "return": {"description": "Description of `return` value.", "type": "int"},
    }


def sample_google_multiline_descriptions(arg1=None, arg2=None):
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
    return {
        "description": "Example of a Google-style docstring.",
        "args": {
            "arg1": {
                "description": "Description of `arg1`. This is an extended description of `arg1`. It can also span multiple lines.",
                "type": "str",
            },
            "arg2": {"description": "Description of `arg2`.", "type": "int"},
        },
        "return": {"type": "", "description": ""},
    }
