# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Global configuration for dep5convert testsuite.
"""


import pathlib
import sys


# add folder with module source to sys.path
srcdir = pathlib.Path(__file__).parents[1].joinpath('src').resolve()
sys.path.insert(0, srcdir.as_posix())
