# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

# General config
extensions = [
    "sphinx.ext.autodoc",   # Auto-generate docs from docstrings
    "sphinx.ext.napoleon",  # Google-style docstrings
    "sphinx.ext.viewcode",  # Add links to source code
    "autoapi.extension"    # Automatically generate API docs
]

# Auto-generate API docs
autoapi_dirs = ["../../savepip"]
autoapi_type = "python"
autoapi_options = ["members", "undoc-members", "show-inheritance"]

project = 'savepip'
copyright = '2025, Adil Alami, Achraf Mataich'
author = 'Adil Alami, Achraf Mataich'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
