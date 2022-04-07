"""
docstring-utils: Parser for Numpy, Sphinx, and Google-style docstrings
"""

from .parsed_docstring import ParsedDocstring, ParsedArgument, ParsedReturnValue
from .parser import parse_docstring

__version__ = "0.0.1"

__all__ = [
    "__version__",
    "ParsedDocstring",
    "ParsedArgument",
    "ParsedReturnValue",
    "parse_docstring",
]
