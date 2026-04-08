# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, os.path.abspath("../../.."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

PYPROJECT_PATH = Path(__file__).parent.parent.parent.parent / "pyproject.toml"

project = "dealme"
copyright = "2026, Curtis Brinker"
author = "Curtis Brinker"

with PYPROJECT_PATH.open("rb") as f:
    pyproject_data = tomllib.load(f)

version = pyproject_data["project"]["version"]
release = version

print("dealme version::", version)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.duration",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "myst_parser",
]

templates_path: list[str] = ["_templates"]
exclude_patterns: list[str] = []

autoclass_content = "both"
autodoc_typehints = "description"
audodoc_verbose = True

modindex_common_prefix = ["dealme."]

todo_include_todos = True

# -- MyST configuration ------------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "dollarmath",
    "colon_fence",
    "deflist",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
