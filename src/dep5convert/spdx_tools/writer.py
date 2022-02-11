# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains a writer for SPDX documents.
"""


from .classes import SPDXDocument


def write_spdx(spdx_document: SPDXDocument) -> str:
    """
    Creates a SPDX formatted string from a :class:`~.spdx_tools.SPDXDcoument`.

    Args:
        spdx_document: :class:`~.spdx_tools.SPDXDcoument` to write as a string.

    Returns:
        A string formatted as SPDX document.
    """
    # pylint: disable=unnecessary-pass,unused-argument
    pass  # via Jinja2?
