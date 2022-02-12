# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
DEP5-specific classes for the Copyright And License Intermediate Representation (CALIR).
"""


class SingleFileMetadataDEP5:
    """
    DEP5-specific CALIR Metadata for a single file.

    Args:
        comment: See :obj:`.dep5_tools.DEP5FilesParagraph.comment`.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self,
                 comment: str = None,
                 ) -> None:
        self._comment = comment

    @property
    def comment(self) -> str:
        """
        Corresponds to :obj:`.dep5_tools.DEP5FilesParagraph.comment`.
        """
        return self._comment


class FileCollectionMetadataDEP5:
    """
    DEP5-specific CALIR Metadata for a file collection.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        pass


class CALIRMetadataDEP5:
    """
    DEP5-specific CALIR Metadata for a CALIR object.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        pass
