# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
SPDX-specific classes for the Copyright And License Intermediate Representation (CALIR).
"""


class SingleFileMetadataSPDX:
    """
    SPDX-specific CALIR Metadata for a single file.

    Args:
        sha1_checksum: See :obj:`.spdx_tools.SPDXFileParagraph.sha1_checksum`.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self,
                 sha1_checksum: str,
                 ) -> None:
        self._sha1_checksum = sha1_checksum

    @property
    def sha1_checksum(self) -> str:
        """
        Corresponds to :obj:`.spdx_tools.SPDXFileParagraph.sha1_checksum`.
        """
        return self._sha1_checksum


class FileCollectionMetadataSPDX:
    """
    SDPX-specific CALIR Metadata for a file collection.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        pass


class CALIRMetadataSPDX:
    """
    SDPX-specific CALIR Metadata for a CALIR object.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        pass
