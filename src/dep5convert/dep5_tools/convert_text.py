# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains a convert functions between :class:`~.dep5_tools.DEP5Document` and text.
"""


from io import StringIO, TextIOBase

import headerparser

from .classes import DEP5Document, DEP5Metadata, DEP5FilesParagraph, _DEP5_FORMAT_URL


class DEP5ParseError(ValueError):
    """
    Raised when a DEP5 text could not be parsed.
    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def parse_dep5(dep5_text: TextIOBase) -> DEP5Document:
    """
    Parses a DEP5 formatted string to create a :class:`~.dep5_tools.DEP5Document`.

    Args:
        dep5_text: Text to parse.

    Returns:
        The newly created :class:`~.dep5_tools.DEP5Document`.
    """
    # pylint: disable=too-many-branches
    stanzas = list[tuple[str, str]]()
    for stanza in headerparser.scan_stanzas(dep5_text):
        stanzas.append(stanza)

    # header paragrah
    dep5_metadata = DEP5Metadata()
    for keyval in stanzas[0]:
        if keyval[0] == 'Format':
            if keyval[1] != _DEP5_FORMAT_URL:
                raise DEP5ParseError('Format does not equal Debian\'s official URI.')
        elif keyval[0] == 'Upstream-Name':
            dep5_metadata.upstream_name = keyval[1]
        elif keyval[0] == 'Upstream-Contact':
            dep5_metadata.upstream_contact = keyval[1]
        elif keyval[0] == 'Source':
            dep5_metadata.source = keyval[1]
        elif keyval[0] == 'Disclaimer':
            dep5_metadata.disclaimer = keyval[1]
        elif keyval[0] == 'Comment':
            dep5_metadata.comment = keyval[1]
        elif keyval[0] == 'License':
            dep5_metadata.license = keyval[1]
        elif keyval[0] == 'Copyright':
            dep5_metadata.copyright = keyval[1]
        elif 'Files-Excluded' in keyval[0]:
            raise DEP5ParseError('Files-Excluded field is not supported.')
        else:
            raise DEP5ParseError(f'Field {keyval[0]} is not known.')

    # file and license paragraphs
    dep5_document = DEP5Document(dep5_metadata)
    for stanza in stanzas[1:]:
        if stanza[0][0] == 'Files':
            files = stanza[0][1]  # split entries
            copyright = stanza[1][1]  # split entries
            license = stanza[2][1]
            comment = None
            if len(stanza) == 4:
                comment = stanza[3][1]
            files_paragraph = DEP5FilesParagraph(files, copyright, license, comment)
            dep5_document.append_files_paragraph(files_paragraph)
        elif stanza[0][0] == 'License':
            pass
        else:
            raise DEP5ParseError(f'Unknown paragraph starting with {stanza[0][0]}.')

    return dep5_document


def write_dep5(dep5_document: DEP5Document, license_paragrahs: bool = False, simplify: bool = True) -> StringIO:
    """
    Creates a DEP5 formatted string from a :class:`~.dep5_tools.DEP5Document`.

    Args:
        dep5_document: :class:`~.dep5_tools.DEP5Document` to write as a string.
        license_paragrahs: If :obj:`True`, also write the license paragrahs.
        simplify: If :obj:`True`, run :func:`.dep5_tools.DEP5Document.simplify` before writing.

    Returns:
        A text stream with the DEP5 document.
    """
    output = StringIO()

    if simplify:
        dep5_document.simplify()

    # header paragraph
    output.write(f'Format: {dep5_document.header_paragraph.format}\n')
    if dep5_document.header_paragraph.upstream_name is not None:
        output.write(f'Upstream-Name: {dep5_document.header_paragraph.upstream_name}\n')
    if dep5_document.header_paragraph.upstream_contact is not None:
        output.write(f'Upstream-Contact: {dep5_document.header_paragraph.upstream_contact}\n')
    if dep5_document.header_paragraph.source is not None:
        output.write(f'Upstream-Name: {dep5_document.header_paragraph.source}\n')
    if dep5_document.header_paragraph.disclaimer is not None:
        output.write(f'Disclaimer: {dep5_document.header_paragraph.disclaimer}\n')
    if dep5_document.header_paragraph.comment is not None:
        output.write(f'Comment: {dep5_document.header_paragraph.comment}\n')
    if dep5_document.header_paragraph.license is not None:
        output.write(f'License: {dep5_document.header_paragraph.license}\n')
    if dep5_document.header_paragraph.copyright is not None:
        output.write(f'Copyright: {dep5_document.header_paragraph.copyright}\n')

    # files paragraphs
    for file_paragraph in dep5_document.files_paragraphs:
        output.write(f'\nFiles: {file_paragraph.files}\n')
        output.write(f'Copyright: {file_paragraph.copyright}\n')
        output.write(f'License: {file_paragraph.license}\n')
        if file_paragraph.comment is not None:
            output.write(f'Comment: {file_paragraph.comment}\n')

    # license paragraphs
    if license_paragrahs:
        pass  # pylint: disable=unnecessary-pass

    return output
