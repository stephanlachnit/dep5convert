# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
dep5convert is a module for converting DEP5-style copyright files.
"""


import pkg_resources

from . import dep5_tools, spdx_tools


__all__ = ['dep5_tools', 'spdx_tools']

_VERSION = pkg_resources.get_distribution(__name__).version
