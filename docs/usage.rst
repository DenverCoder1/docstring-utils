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

    result = parse_docstring(example, filter_args=True)

    print(result.description)  # "Example of a Google-style docstring."

    args = result.args.values()
    print(args[0].name)  # "arg1"
    print(args[0].description)  # "Description of `arg1`."
    print(args[0].type)  # "str"

    print(result.return_value.type)  # "int"
    print(result.return_value.description)  # "Description of `return` value."