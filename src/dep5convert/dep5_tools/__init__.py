# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
This module contains tools to manipulate DEP5 documents.
"""


from .classes import DEP5Document, DEP5FilesParagraph, DEP5HeaderParagraph, DEP5LicenseParagraph, DEP5Metadata
from .convert_calir import convert_calir_to_dep5, convert_dep5_to_calir
from .convert_text import parse_dep5, write_dep5


__all__ = [
    'convert_calir_to_dep5',
    'convert_dep5_to_calir',
    'DEP5Document',
    'DEP5FilesParagraph',
    'DEP5HeaderParagraph',
    'DEP5LicenseParagraph',
    'DEP5Metadata',
    'parse_dep5',
    'write_dep5',
]
