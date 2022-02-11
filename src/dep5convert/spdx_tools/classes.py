# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Classes holding the information of a SPDX document.
"""


class SPDXHeaderParagraph:
    """
    Class containing the header paragraph of a SPDX document.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        pass


class SPDXFileParagraph:
    """
    Class containing a single file paragraph of a SPDX document.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self,
                 file_name: str,
                 spdx_id: str,
                 sha1_checksum: str,
                 ) -> None:
        self._file_name = file_name
        self._spdx_id = spdx_id
        self._sha1_checksum = sha1_checksum

    @property
    def file_name(self) -> str:
        """
        The file name.
        """
        return self._file_name

    @property
    def spdx_id(self) -> str:
        """
        The SPDX ID of the file.
        """
        return self._spdx_id

    @property
    def sha1_checksum(self) -> str:
        """
        SHA1 checksum of the file.
        """
        return self._sha1_checksum


class SPDXDocument:
    """
    Class holding all the information of a SPDX document.

    Args:
        header_paragraph: The header paragraph of the document.
        file_paragraphs: List of file paragraphs in the document.
    """
    def __init__(self,
                 header_paragraph: SPDXHeaderParagraph,
                 file_paragraphs: list[SPDXFileParagraph] = None,
                 ) -> None:
        self._header_paragraph = header_paragraph
        self._file_paragraphs = file_paragraphs

        if self._file_paragraphs is None:
            self._file_paragraphs = list[SPDXFileParagraph]()

    @property
    def header_paragraph(self) -> SPDXHeaderParagraph:
        """
        Header paragraph of the document.
        """
        return self._header_paragraph

    @property
    def file_paragraphs(self) -> list[SPDXFileParagraph]:
        """
        List of file paragraphs of the document.
        """
        return self._file_paragraphs

    def append_file_paragraph(self, file_paragraph: SPDXFileParagraph) -> None:
        """
        Appends a file paragraph to the document.

        Args:
            file_paragraph: The files paragraph to add.

        """
        self._file_paragraphs.append(file_paragraph)
