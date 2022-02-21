# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: CC0-1.0

"""
Configuration for the dep5convert sphinx documentation.
"""

# pylint: disable=invalid-name


import pathlib
import sys

import pkg_resources


# add folder with module source to sys.path
srcdir = pathlib.Path(__file__).parents[2].joinpath('src').resolve()
sys.path.insert(0, srcdir.as_posix())

# project metadata
project = 'dep5convert'
project_copyright = '2022 Stephan Lachnit, CC-BY-SA-4.0'
author = 'Stephan Lachnit'
version = pkg_resources.get_distribution('dep5convert').version

# extensions
extensions = [
    'myst_parser',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_paramlinks',
    'sphinxcontrib.apidoc',
]

# general settings
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# HTML settings
html_theme = 'sphinx_rtd_theme'

# sphinx.ext.autosectionlabel settings
autosectionlabel_prefix_document = True

# sphinx.ext.intersphinx settings
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# sphinxcontrib.apidoc settings
apidoc_module_dir = srcdir.joinpath('dep5convert').as_posix()
apidoc_separate_modules = True
