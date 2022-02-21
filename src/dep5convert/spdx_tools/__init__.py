# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
This module contains tools to manipulate SPDX documents.
"""


from .classes import SPDXDocument, SPDXHeaderParagraph, SPDXFileParagraph


__all__ = [
    'SPDXDocument',
    'SPDXHeaderParagraph',
    'SPDXFileParagraph',
]
