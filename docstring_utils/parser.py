import inspect
import re
from functools import cached_property
from typing import Any, Callable, Dict

from .parsed_docstring import ParsedDocstring
from .utils import find

_SHORT_DESCRIPTION_REGEX = re.compile(r"\A(?:.|\n)+?(?=\Z|\r?\n\r?\n)", re.MULTILINE)

_ARG_NAME_SUBREGEX = r"(?:\\?\*)*(?P<name>[^\s:\-]+)"

_ARG_DESCRIPTION_SUBREGEX = r"(?P<description>(?:.|\n)+?(?:\Z|\r?\n(?=[\S\r\n])))"

_ARG_TYPE_SUBREGEX = r"(?P<type>.+)"

_GOOGLE_SECTION_REGEX = re.compile(
    r"^(?P<section_name>[\w ]+):\s*\r?\n(?P<body>.+?(?:\Z|(?=\r?\n?^\w)))",
    re.MULTILINE | re.DOTALL,
)

_NUMPY_SECTION_REGEX = re.compile(
    r"^(?P<section_name>\w+)\s*\r?\n-+\r?\n(?P<body>.+?(?:\Z|(?=\r?\n?^\w+\s*\r?\n-+)))",
    re.MULTILINE | re.DOTALL,
)

_GOOGLE_DOCSTRING_ARG_REGEX = re.compile(
    rf"^{_ARG_NAME_SUBREGEX}[ \t]*(?:\({_ARG_TYPE_SUBREGEX}\))?[ \t]*:[ \t]*{_ARG_DESCRIPTION_SUBREGEX}",
    re.MULTILINE,
)

_SPHINX_DOCSTRING_ARG_REGEX = re.compile(
    rf"^:param {_ARG_NAME_SUBREGEX}:[ \t]+{_ARG_DESCRIPTION_SUBREGEX}[ \t]*(?::type [^\s:]+:[ \t]+{_ARG_TYPE_SUBREGEX})?",
    re.MULTILINE,
)

_SPHINX_DOCSTRING_RETURN_REGEX = re.compile(
    rf"^:return {_ARG_NAME_SUBREGEX}:[ \t]+{_ARG_DESCRIPTION_SUBREGEX}[ \t]*(?::rtype [^\s:]+:[ \t]+{_ARG_TYPE_SUBREGEX})?",
    re.MULTILINE,
)

_NUMPY_DOCSTRING_ARG_REGEX = re.compile(
    rf"^{_ARG_NAME_SUBREGEX}(?:[ \t]*:)?(?:[ \t]+{_ARG_TYPE_SUBREGEX})?[ \t]*\r?\n[ \t]+{_ARG_DESCRIPTION_SUBREGEX}",
    re.MULTILINE,
)

_PARAMETER_SECTION_NAMES = ("Args", "Arguments", "Parameters", "Other Parameters")

_RETURN_SECTION_NAMES = ("Returns", "Return")


class _DocstringParser:
    """A parser class for docstrings

    Parameters
    ------------
    func: Callable[..., Any]
        The function to parse the docstring of
    filter_args: :class:`bool`
        Whether to filter out arguments that are not in the function signature
    """

    def __init__(self, func: Callable[..., Any], *, filter_args: bool = False):
        self._func = func
        self._filter_args = filter_args
        self._docstring = inspect.cleandoc(inspect.getdoc(self._func) or "").strip()

    @cached_property
    def parsed_docstring(
        self,
    ) -> ParsedDocstring:
        """Parses the docstring of a function into a dictionary

        Returns
        --------
        :class:`ParsedDocstring`
            The parsed docstring
        """
        data = {}

        # Parse the docstring only if it is not empty
        if self._docstring:
            data = {
                "description": self._parsed_short_description,
                "args": self._parsed_arguments,
                "return": self._parsed_return,
            }

        return ParsedDocstring(self._docstring, data)

    @cached_property
    def _parsed_short_description(self) -> str:
        """Parses the short description of the funcion

        Returns
        -------
        :class:`str`
            The short description of the function
        """
        description_match = _SHORT_DESCRIPTION_REGEX.search(self._docstring)
        if not description_match:
            return ""
        return re.sub(r"\n\s*", " ", description_match.group(0)).strip()

    @cached_property
    def _parsed_arguments(self) -> Dict[str, Dict[str, str]]:
        # Extract the sections of the docstring of Google / Numpy type
        google_sections = self._parsed_sections_google
        numpy_sections = self._parsed_sections_numpy

        # Extract the arguments sections from the docstring
        google_arguments_section = self._arguments_section(google_sections)
        numpy_arguments_section = self._arguments_section(numpy_sections)

        # Find argument matches
        docstring_argument_styles = [
            _GOOGLE_DOCSTRING_ARG_REGEX.finditer(google_arguments_section),
            _NUMPY_DOCSTRING_ARG_REGEX.finditer(numpy_arguments_section),
            _SPHINX_DOCSTRING_ARG_REGEX.finditer(self._docstring),
        ]

        # Choose the style with the largest number of arguments matched
        matched_args = []
        actual_args = inspect.signature(self._func).parameters.keys()
        for matches in docstring_argument_styles:
            style_matched_args = [
                match
                for match in matches
                if not self._filter_args or match.group("name") in actual_args
            ]
            if len(style_matched_args) > len(matched_args):
                matched_args = style_matched_args

        # Create the argument dictionary
        args: Dict[str, Dict[str, str]] = {}
        for arg in matched_args:
            arg_description = re.sub(r"\n\s*", " ", arg.group("description")).strip()
            args[arg.group("name")] = {
                "description": arg_description,
                "type": arg.group("type") or "",
            }

        return args

    @cached_property
    def _parsed_return(self) -> Dict[str, str]:
        """Parses the return section of the docstring

        Returns
        -------
        :class:`Dict[str, str]`
            The parsed return section of the docstring
        """
        # Extract the sections of the docstring of Google / Numpy type
        google_sections = self._parsed_sections_google
        numpy_sections = self._parsed_sections_numpy

        # Extract the arguments sections from the docstring
        google_return_section = self._return_section(google_sections)
        numpy_return_section = self._return_section(numpy_sections)

        # Find return matches
        docstring_return_styles = [
            _GOOGLE_DOCSTRING_ARG_REGEX.match(google_return_section),
            _NUMPY_DOCSTRING_ARG_REGEX.match(numpy_return_section),
            _SPHINX_DOCSTRING_RETURN_REGEX.match(self._docstring),
        ]

        matched_style = find(lambda style: style is not None, docstring_return_styles)

        if not matched_style:
            return {}

        return {
            "description": matched_style.group("description").strip(),
            "type": matched_style.group("name") or "",
        }

    @cached_property
    def _parsed_sections_google(self) -> Dict[str, str]:
        """Parses the docstring into sections using Google style

        Returns
        --------
        :class:`Dict[str, str]`
            Mapping of section names to section contents
        """
        return {
            match.group("section_name"): inspect.cleandoc(match.group("body"))
            for match in _GOOGLE_SECTION_REGEX.finditer(self._docstring)
        }

    @cached_property
    def _parsed_sections_numpy(self) -> Dict[str, str]:
        """Parses the docstring into sections using Numpy style

        Returns
        --------
        :class:`Dict[str, str]`
            Mapping of section names to section contents
        """
        return {
            match.group("section_name"): match.group("body")
            for match in _NUMPY_SECTION_REGEX.finditer(self._docstring)
        }

    def _arguments_section(self, sections: Dict[str, str]) -> str:
        """Extract the combined arguments sections of the docstring

        Parameters
        -----------
        sections: :class:`Dict[str, str]`
            The sections of the docstring as returned by
            :meth:`_parse_sections_google` or :meth:`_parse_sections_numpy`

        Returns
        --------
        :class:`str`
            The combined arguments sections of the docstring
        """
        return "\n".join(
            body
            for section, body in sections.items()
            if section in _PARAMETER_SECTION_NAMES
        )

    def _return_section(self, sections: Dict[str, str]) -> str:
        """Extract the combined return sections of the docstring

        Parameters
        -----------
        sections: :class:`Dict[str, str]`
            The sections of the docstring as returned by
            :meth:`_parse_sections_google` or :meth:`_parse_sections_numpy`

        Returns
        --------
        :class:`str`
            The combined return sections of the docstring
        """
        return_key = find(lambda s: s in _RETURN_SECTION_NAMES, sections)
        return sections.get(return_key, "") if return_key else ""


def parse_docstring(
    func: Callable[..., Any], *, filter_args: bool = False
) -> ParsedDocstring:
    """Parses the docstring of a function into a dictionary

    Parameters
    ------------
    func: Callable[..., Any]
        The function to parse the docstring of
    filter_args: :class:`bool`
        Whether to filter out arguments that are not in the function signature

    Returns
    --------
    :class:`ParsedDocstring`
        The parsed docstring
    """
    return _DocstringParser(func, filter_args=filter_args).parsed_docstring
