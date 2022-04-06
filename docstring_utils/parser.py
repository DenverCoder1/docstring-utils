import inspect
import re
from typing import Any, Callable, Dict

_SHORT_DESCRIPTION_REGEX = re.compile(r"\A(?:.|\n)+?(?=\Z|\r?\n\r?\n)", re.MULTILINE)

_ARG_NAME_SUBREGEX = r"(?:\\?\*)*(?P<name>[^\s:\-]+)"

_ARG_DESCRIPTION_SUBREGEX = r"(?P<description>(?:.|\n)+?(?:\Z|\r?\n(?=[\S\r\n])))"

_ARG_TYPE_SUBREGEX = r"(?P<type>.+)"

_GOOGLE_DOCSTRING_ARG_REGEX = re.compile(
    rf"^{_ARG_NAME_SUBREGEX}[ \t]*(?:\({_ARG_TYPE_SUBREGEX}\))?[ \t]*:[ \t]*{_ARG_DESCRIPTION_SUBREGEX}",
    re.MULTILINE
)

_SPHINX_DOCSTRING_ARG_REGEX = re.compile(
    rf"^:param {_ARG_NAME_SUBREGEX}:[ \t]+{_ARG_DESCRIPTION_SUBREGEX}[ \t]*(?::type [^\s:]+:[ \t]+{_ARG_TYPE_SUBREGEX})?",
    re.MULTILINE
)

_NUMPY_DOCSTRING_ARG_REGEX = re.compile(
    rf"^{_ARG_NAME_SUBREGEX}(?:[ \t]*:)?(?:[ \t]+{_ARG_TYPE_SUBREGEX})?[ \t]*\r?\n[ \t]+{_ARG_DESCRIPTION_SUBREGEX}",
    re.MULTILINE
)


def parse_docstring(func: Callable, *, filter_args: bool = False) -> Dict[str, Any]:
    """Parses the docstring of a function into a dictionary.

    Parameters
    ------------
    func: :class:`Callable`
        The function to parse the docstring of.
    filter_args: :class:`bool`
        Whether to filter out arguments that are not in the function signature.

    Returns
    --------
    :class:`Dict[str, Any]`
        The parsed docstring including the function description and
        descriptions of arguments.
    """
    description = ""
    args = {}

    if docstring := inspect.cleandoc(inspect.getdoc(func) or "").strip():
        # Extract the function description
        description_match = _SHORT_DESCRIPTION_REGEX.search(docstring)
        if description_match:
            description = re.sub(r"\n\s*", " ", description_match.group(0)).strip()

        # Extract the arguments
        # For Google-style, look only at the lines that are indented
        section_lines = inspect.cleandoc("\n".join(line for line in docstring.splitlines() if line.startswith(("\t", "  "))))
        docstring_styles = [
            _GOOGLE_DOCSTRING_ARG_REGEX.finditer(section_lines),
            _SPHINX_DOCSTRING_ARG_REGEX.finditer(docstring),
            _NUMPY_DOCSTRING_ARG_REGEX.finditer(docstring),
        ]

        # choose the style with the largest number of arguments matched
        matched_args = []
        actual_args = inspect.signature(func).parameters.keys()
        for matches in docstring_styles:
            style_matched_args = [
                match
                for match in matches
                if not filter_args or match.group("name") in actual_args
            ]
            if len(style_matched_args) > len(matched_args):
                matched_args = style_matched_args

        for arg in matched_args:
            arg_description = re.sub(r"\n\s*", " ", arg.group("description")).strip()
            args[arg.group("name")] = {
                "description": arg_description,
                "type": arg.group("type"),
            }

    return {"description": description, "args": args}
