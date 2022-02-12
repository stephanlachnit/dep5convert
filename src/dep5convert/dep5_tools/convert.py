# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains converters between DEP5 and CALIR.
"""


from .classes import DEP5Document
from ..calir import CALIR, CALIRMetadataDEP5


def convert_dep5_to_calir(dep5_document: DEP5Document) -> CALIR:
    """
    Converts a :class:`~.dep5_tools.DEP5Document` to the :class:`~.calir.CALIR`.

    Args:
        dep5_document: :class:`~.dep5_tools.DEP5Document` to convert.

    Returns:
        The newly created :class:`~.calir.CALIR`.
    """
    # pylint: disable=unnecessary-pass,unused-argument
    pass


def convert_calir_to_dep5(calir_obj: CALIR, metadata: CALIRMetadataDEP5 = None) -> DEP5Document:
    """
    Converts from the :class:`~.calir.CALIR` to a :class:`~.dep5_tools.DEP5Document`.

    Args:
        calir_obj: :class:`~.calir.CALIR` to convert.
        metadata: Optional metadata for the :class:`~.dep5_tools.DEP5Document`.

    Returns:
        The newly created :class:`~.dep5_tools.DEP5Document`.
    """
    # pylint: disable=unnecessary-pass,unused-argument
    pass
