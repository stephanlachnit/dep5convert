# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains a writer for DEP5 documents.
"""


from .classes import DEP5Document


def write_dep5(dep5_document: DEP5Document) -> str:
    """
    Creates a DEP5 formatted string from a :class:`~.dep5_tools.DEP5Document`.

    Args:
        dep5_document: :class:`~.dep5_tools.DEP5Document` to write as a string.

    Returns:
        A string formatted as DEP5 document.
    """
    # pylint: disable=unnecessary-pass,unused-argument
    pass  # via Jinja2?
