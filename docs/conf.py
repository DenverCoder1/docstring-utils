# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from typing import List

sys.path.insert(0, os.path.abspath("../.."))
sys.path.append(os.path.abspath("extensions"))


# -- Project information -----------------------------------------------------

project = "docstring-utils"
copyright = "2022, Jonah Lawrence"
author = "Jonah Lawrence"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
    "sphinx_book_theme",
    "sphinxext.opengraph",
    "attributetable",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
highlight_language = "python3"
html_theme = "sphinx_book_theme"
master_doc = "index"
pygments_style = "friendly"
source_suffix = ".rst"

html_theme_options = {
    "repository_url": "https://github.com/DenverCoder1/docstring-utils",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for EPUB output
epub_show_urls = "footnote"


def uncached(directory: str, files: List[str]) -> List[str]:
    """Append last modified date to filenames in order to prevent caching old versions"""
    return [
        f'{directory}/{filename}?v={os.path.getmtime(os.path.join("_static", directory, filename))}'
        for filename in files
    ]


html_css_files = uncached("css", ["custom.css"])

html_js_files = uncached("js", ["darkreader.min.js", "toggleDarkMode.js"])
