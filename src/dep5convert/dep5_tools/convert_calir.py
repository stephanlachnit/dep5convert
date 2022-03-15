# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains converters between DEP5 and CALIR.
"""


from pathlib import Path

from ..calir import CALIR, CALIRSingle
from .classes import DEP5Document, DEP5FilesParagraph, DEP5Metadata
from .util import guess_license_expression


def convert_calir_to_dep5(calir: CALIR, metadata: DEP5Metadata) -> DEP5Document:
    dep5_dokument = DEP5Document(metadata)
    for single in calir.singles:
        dep5_dokument.append_files_paragraph(DEP5FilesParagraph([single.path], single.copyright, single.license))
    return dep5_dokument


def convert_dep5_to_calir(dep5_document: DEP5Document, source_path: Path = None) -> CALIR:
    calir = CALIR()
    dep5_document.expand_globs(source_path)
    for files_paragraph in dep5_document.files_paragraphs:
        license = guess_license_expression(files_paragraph.license)
        for file in files_paragraph.files:
            path = Path(file)
            single = CALIRSingle(path, files_paragraph.copyright, license)
            calir.add_single(single, overwrite=True)
    return calir
