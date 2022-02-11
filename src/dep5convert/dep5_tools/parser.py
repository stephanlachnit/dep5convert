# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains a parser for DEP5 documents.
"""


from .classes import DEP5Document


def parse_dep5(dep5_string: str) -> DEP5Document:
    """
    Parses a DEP5 formatted string to create a :class:`~.dep5_tools.DEP5Document`.

    Args:
        dep5_string: String to parse.

    Returns:
        The newly created :class:`~.dep5_tools.DEP5Document`.
    """
    # pylint: disable=unnecessary-pass,unused-argument
    pass
