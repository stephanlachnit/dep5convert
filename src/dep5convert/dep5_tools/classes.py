# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Classes holding the information of a DEP5 document.
"""

# pylint: disable=redefined-builtin


from . import _util


class DEP5HeaderParagraph:
    """
    Class containing the header paragraph of a DEP5 document.
    """
    def __init__(self,
                 upstream_name: str = None,
                 upstream_contact: list[str] = None,
                 source: str = None,
                 disclaimer: str = None,
                 comment: str = None,
                 license: str = None,
                 copyright: str = None,
                 ) -> None:
        self._format = _util.DEP5_FORMAT_URL
        self._upstream_name = upstream_name
        self._upstream_contact = upstream_contact
        self._source = source
        self._disclaimer = disclaimer
        self._comment = comment
        self._license = license
        self._copyright = copyright

    @property
    def format(self) -> str:
        """
        URI of the format specification. Always points to the official Debian specification.
        """
        return self._format

    @property
    def upstream_name(self) -> str:
        """
        The name upstream uses for the software.
        """
        return self._upstream_name

    @property
    def upstream_contact(self) -> list[str]:
        """
        The preferred addresses to reach the upstream project. Typically RFC5322 addresses or URIs.
        """
        return self._upstream_contact

    @property
    def source(self) -> str:
        """
        Explanation of where the upstream source came from. Typically a URL.
        """
        return self._upstream_name

    @property
    def disclaimer(self) -> str:
        """
        Field for non-free or contrib packages to state that they are not part of Debian and to explain why.
        """
        return self._disclaimer

    @property
    def comment(self) -> str:
        """
        Field that can provide additional information.
        """
        return self._comment

    @property
    def license(self) -> str:
        """
        License information for the package as a whole.
        Same format as :obj:`DEP5FilesParagraph.license`.
        """
        return self._license

    @property
    def copyright(self) -> str:
        """
        Copyright information for the package as a whole.
        Same format as :obj:`DEP5FilesParagraph.copyright`.
        """
        return self._copyright


class DEP5FilesParagraph:
    """
    Class containing a single files paragraph of a DEP5 document.
    """
    def __init__(self,
                 files: list[str],
                 copyright: list[str],
                 license: str,
                 comment: str = None,
                 ) -> None:
        self._files = files
        self._copyright = copyright
        self._license = license
        self._comment = comment

    @property
    def files(self) -> list[str]:
        """
        List of patterns indicating files covered by the license and copyright specified in this paragraph.
        """
        return self._files

    @property
    def copyright(self) -> list[str]:
        """
        List of free-form copyright statements. Typically in the form "%(years) %(author)s <%(contact)s>"
        """
        return self._copyright

    @property
    def license(self) -> str:
        """
        Short name for the license, maybe be followed by the license text starting in the next line.
        """
        return self._license

    @property
    def comment(self) -> str:
        """
        Field that can provide additional information.
        """
        return self._comment


class DEP5LicenseParagraph:
    """
    Class containing a single license paragraph of a DEP5 document.
    """
    def __init__(self,
                 license: str,
                 comment: str = None,
                 ) -> None:
        self._license = license
        self._comment = comment

    @property
    def license(self) -> str:
        """
        Short name for the license, followed by the license text starting in the next line.
        """
        return self._license

    @property
    def comment(self) -> str:
        """
        Field that can provide additional information.
        """
        return self._comment


class DEP5Document:
    """
    Class holding all the information of a DEP5 document.

    Args:
        header_paragraph: The header paragraph of the document.
        files_paragraphs: List of files paragraphs in the document. Can be :obj:`None` or empty.
        license_paragraphs: List of license paragraphs in the document. Can be :obj:`None` or empty.
    """
    def __init__(self,
                 header_paragraph: DEP5HeaderParagraph,
                 files_paragraphs: list[DEP5FilesParagraph] = None,
                 license_paragraphs: list[DEP5LicenseParagraph] = None,
                 ) -> None:
        self._header_paragraph = header_paragraph
        self._files_paragraphs = files_paragraphs
        self._license_paragraphs = license_paragraphs

        if self._files_paragraphs is None:
            self._files_paragraphs = list[DEP5FilesParagraph]()
        if self._license_paragraphs is None:
            license_paragraphs = list[DEP5LicenseParagraph]()

    @property
    def header_paragraph(self) -> DEP5HeaderParagraph:
        """
        Header paragraph of the document.
        """
        return self._header_paragraph

    @property
    def files_paragraphs(self) -> list[DEP5FilesParagraph]:
        """
        List of files paragraphs of the document.
        """
        return self._files_paragraphs

    @property
    def license_paragraphs(self) -> list[DEP5LicenseParagraph]:
        """
        List of license paragraphs of the document.
        """
        return self._license_paragraphs

    def append_files_paragraph(self, files_paragraph: DEP5FilesParagraph) -> None:
        """
        Appends a files paragraph to the document.

        Args:
            files_paragraph: The files paragraph to add.

        """
        self._files_paragraphs.append(files_paragraph)

    def append_license_paragraph(self, license_paragraph: DEP5LicenseParagraph) -> None:
        """
        Appends a license paragraph to the document.

        Args:
            license_paragraph: The license paragraph to add.

        """
        self._license_paragraphs.append(license_paragraph)
