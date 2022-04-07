# docstring-utils

[![build](https://img.shields.io/github/workflow/status/DenverCoder1/docstring-utils/Python%20application/main)](https://github.com/DenverCoder1/docstring-utils/actions/workflows/python-app.yml)
[![version](https://img.shields.io/pypi/v/docstring-utils)](https://pypi.org/project/docstring-utils/)
[![license](https://img.shields.io/pypi/l/docstring-utils)](https://github.com/DenverCoder1/docstring-utils/blob/main/LICENSE)
[![discord](https://img.shields.io/discord/819650821314052106?color=5865F2&logo=discord&logoColor=white "Dev Pro Tips Discussion & Support Server")](https://discord.gg/fPrdqh3Zfu)

Simple parser for Numpy, Sphinx, and Google-style docstrings

## 📥 Installation

`pip install -U docstring-utils`

**Requirements:** `Python 3.7+`

## 🧑‍💻 Usage

### Parse docstring

```py
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
```

## 🧰 Development

### Running tests

1. Install `tox` with the command `pip install -U tox`

2. Run tests with the command `tox`

### Linting

Run the following command to lint with flake8

`python setup.py lint`

(Note: The exact command may vary depending on your Python version and environment)
