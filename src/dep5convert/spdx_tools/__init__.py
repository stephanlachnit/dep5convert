# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
This module contains tools to manipulate SPDX documents.
"""


from .classes import SPDXDocument, SPDXHeaderParagraph, SPDXFileParagraph
from .parser import parse_spdx
from .writer import write_spdx


__all__ = [
    'SPDXDocument',
    'SPDXHeaderParagraph',
    'SPDXFileParagraph',
    'parse_spdx',
    'write_spdx',
]
