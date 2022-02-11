# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains a parser for SPDX documents.
"""


from .classes import SPDXDocument


def parse_spdx(spdx_string: str) -> SPDXDocument:
    """
    Parses a SPDX formatted string to create a :class:`~.spdx_tools.SPDXDcoument`.

    Args:
        spdx_string: String to parse.

    Returns:
        The newly created :class:`~.dep5_tools.SPDXDcoument`.
    """
    # pylint: disable=unnecessary-pass,unused-argument
    pass
