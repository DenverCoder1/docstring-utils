from dataclasses import dataclass
from typing import Any, Dict, Iterator


@dataclass
class ParsedReturnValue:
    """Represents a parsed return value

    Attributes
    ----------
    type: :class:`str`
        The return type.
    description: :class:`str`
        The description of the return value.
    """

    type: str
    description: str

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(type={self.type!r}, description={self.description!r})>"


@dataclass
class ParsedArgument:
    """Represents a parsed argument

    Attributes
    ----------
    name: :class:`str`
        The name of the argument.
    type: :class:`str`
        The type of the argument.
    description: :class:`str`
        The description of the argument.
    """

    name: str
    type: str
    description: str

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name={self.name!r}, type={self.type!r}, description={self.description!r})>"


class ParsedDocstring:
    """
    Class representing a docstring that has been parsed.
    """

    def __init__(self, docstring: str, parsed_docstring: Dict[str, Any]):
        """
        Parameters
        ----------
        docstring: str
            The docstring that was parsed.
        parsed_docstring: Dict[str, Any]
            The parsed docstring.
        """
        self._docstring = docstring
        self._parsed_docstring = parsed_docstring

    @property
    def docstring(self) -> str:
        """:class:`str`: The docstring that was parsed."""
        return self._docstring

    @property
    def description(self) -> str:
        """:class:`str`: The description of the parsed docstring."""
        return self._parsed_docstring["description"]

    @property
    def args(self) -> Dict[str, ParsedArgument]:
        """Dict[:class:`str`, :class:`ParsedArgument`]: The parsed arguments."""
        return {
            name: ParsedArgument(
                name=name, description=arg["description"], type=arg["type"]
            )
            for name, arg in self._parsed_docstring["args"].items()
        }

    @property
    def return_value(self) -> ParsedReturnValue:
        """:class:`ParsedReturnValue`: The parsed return value."""
        return ParsedReturnValue(
            type=self._parsed_docstring["return"]["type"],
            description=self._parsed_docstring["return"]["description"],
        )

    def __getattr__(self, name: str) -> Any:
        """
        Returns
        -------
        Any
            The value of the attribute.
        """
        return self._parsed_docstring[name]

    def __getitem__(self, name: str) -> Any:
        """
        Returns
        -------
        Any
            The value of the attribute.
        """
        return self._parsed_docstring[name]

    def __contains__(self, name: str) -> bool:
        """
        Returns
        -------
        bool
            Whether the attribute exists.
        """
        return name in self._parsed_docstring

    def __iter__(self) -> Iterator[str]:
        """
        Returns
        -------
        Iterator[str]
            An iterator over the parsed docstring.
        """
        return iter(self._parsed_docstring)

    def __len__(self) -> int:
        """
        Returns
        -------
        int
            The length of the parsed docstring.
        """
        return len(self._parsed_docstring)

    def __repr__(self) -> str:
        """
        Returns
        -------
        str
            The representation of the parsed docstring.
        """
        return f"<{self.__class__.__name__}(description='{self.description}', args={self.args}, return_value={self.return_value})>"
