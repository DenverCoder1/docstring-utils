Usage
---------

Parse Docstrings
================

.. code:: python

    from docstring_utils import parse_docstring

    def example(arg1: str, arg2: int) -> int:
        """Example of a Google-style docstring.

        Args:
            arg1 (str): Description of `arg1`.
            arg2 (int): Description of `arg2`.

        Returns:
            int: Description of `return` value.
        """
        return 0

    parse_docstring(example, filter_args=True)

    # Output:
    {
        "description": "Example of a Google-style docstring.",
        "args": {
            "arg1": {
                "description": "Description of `arg1`.",
                "type": "str",
            },
            "arg2": {
                "description": "Description of `arg2`.",
                "type": "int",
            },
        },
        "return": {
            "description": "Description of `return` value.",
            "type": "int",
        },
    }