def sample_sphinx_short_description():
    """Example of a Sphinx-style docstring."""
    return {
        "description": "Example of a Sphinx-style docstring.",
        "args": {},
        "return": {"type": "", "description": ""},
    }


def sample_sphinx_extended_description():
    """Example of a Sphinx-style docstring.

    This is a longer description of what the function or class does. It may
    span multiple lines.
    """
    return {
        "description": "Example of a Sphinx-style docstring.",
        "args": {},
        "return": {"type": "", "description": ""},
    }


def sample_sphinx_argument(arg1=None):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    """
    return {
        "description": "Example of a Sphinx-style docstring.",
        "args": {"arg1": {"description": "Description of `arg1`.", "type": ""}},
        "return": {"type": "", "description": ""},
    }


def sample_sphinx_arguments(arg1=None, arg2=None):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    :param arg2: Description of `arg2`.
    """
    return {
        "description": "Example of a Sphinx-style docstring.",
        "args": {
            "arg1": {"description": "Description of `arg1`.", "type": ""},
            "arg2": {"description": "Description of `arg2`.", "type": ""},
        },
        "return": {"type": "", "description": ""},
    }


def sample_sphinx_arguments_with_types(arg1=None, arg2=None):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    :type arg1: :class:`str`
    :param arg2: Description of `arg2`.
    :type arg2: :class:`int`
    """
    return {
        "description": "Example of a Sphinx-style docstring.",
        "args": {
            "arg1": {"description": "Description of `arg1`.", "type": ":class:`str`"},
            "arg2": {"description": "Description of `arg2`.", "type": ":class:`int`"},
        },
        "return": {"type": "", "description": ""},
    }


def sample_sphinx_return_value(arg1=None):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
    :type arg1: :class:`str`
    :return: Description of `return` value.
    :rtype: :class:`int`
    """
    return {
        "description": "Example of a Sphinx-style docstring.",
        "args": {
            "arg1": {"description": "Description of `arg1`.", "type": ":class:`str`"}
        },
        "return": {"type": "", "description": ""},
    }


def sample_sphinx_multiline_descriptions(arg1=None, arg2=None):
    """Example of a Sphinx-style docstring.

    :param arg1: Description of `arg1`.
        This is a multi-line description.
    :type arg1: :class:`str`
    :param arg2: Description of `arg2`.

        This is a multi-line description. There can be blank lines.
    """
    return {
        "description": "Example of a Sphinx-style docstring.",
        "args": {
            "arg1": {
                "description": "Description of `arg1`. This is a multi-line description.",
                "type": ":class:`str`",
            },
            "arg2": {"description": "Description of `arg2`.", "type": ""},
        },
        "return": {"type": "", "description": ""},
    }
