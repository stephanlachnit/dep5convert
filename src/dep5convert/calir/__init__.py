# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
This module contains tools for the Copyright And License Intermedite Representation (CALIR).
"""


from .classes import CALIR, SinlgeFile, FileCollectionMetadata
from .dep5_metadata import CALIRMetadataDEP5, SingleFileMetadataDEP5, FileCollectionMetadataDEP5
from .spdx_metadata import CALIRMetadataSPDX, SingleFileMetadataSPDX, FileCollectionMetadataSPDX


__all__ = [
    'CALIR',
    'SinlgeFile',
    'FileCollectionMetadata',
    'CALIRMetadataDEP5',
    'SingleFileMetadataDEP5',
    'FileCollectionMetadataDEP5',
    'CALIRMetadataSPDX',
    'SingleFileMetadataSPDX',
    'FileCollectionMetadataSPDX',
]
