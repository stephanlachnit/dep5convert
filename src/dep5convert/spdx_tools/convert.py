# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains converters between SPDX and CALIR.
"""


from .classes import SPDXDocument
from ..calir import CALIR, CALIRMetadataSPDX


def convert_spdx_to_calir(spdx_document: SPDXDocument) -> CALIR:
    """
    Converts a :class:`~.spdx_tools.SPDXDocument` to the :class:`~.calir.CALIR`.

    Args:
        spdx_document: :class:`~.spdx_tools.SPDXDocument` to convert.

    Returns:
        The newly created :class:`~.calir.CALIR`.
    """
    # pylint: disable=unnecessary-pass,unused-argument
    pass


def convert_calir_to_spdx(calir_obj: CALIR, metadata: CALIRMetadataSPDX) -> SPDXDocument:
    """
    Converts from the :class:`~.calir.CALIR` to a :class:`~.spdx_tools.SPDXDocument`.

    Args:
        calir_obj: :class:`~.calir.CALIR` to convert.
        metadata: Required metadata for the :class:`~.spdx_tools.SPDXDocument`.

    Returns:
        The newly created :class:`~.spdx_tools.SPDXDocument`.
    """
    # pylint: disable=unnecessary-pass,unused-argument
    pass
