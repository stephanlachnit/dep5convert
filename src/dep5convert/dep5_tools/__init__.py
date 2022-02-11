# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
This module contains tools to manipulate DEP5 documents.
"""


from .classes import DEP5Document, DEP5HeaderParagraph, DEP5FilesParagraph, DEP5LicenseParagraph
from .parser import parse_dep5
from .writer import write_dep5


__all__ = [
    'DEP5Document',
    'DEP5HeaderParagraph',
    'DEP5FilesParagraph',
    'DEP5LicenseParagraph',
    'parse_dep5',
    'write_dep5',
]
