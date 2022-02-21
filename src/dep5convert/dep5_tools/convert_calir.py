# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains converters between DEP5 and CALIR.
"""


from pathlib import Path

from ..calir import CALIR, CALIRSingle
from .classes import DEP5Document, DEP5FilesParagraph, DEP5Metadata
from .util import expand_dep5_glob, guess_license_expression


def convert_calir_to_dep5(calir: CALIR, metadata: DEP5Metadata) -> DEP5Document:
    dep5_dokument = DEP5Document(metadata)
    for single in calir.singles:
        dep5_dokument.append_files_paragraph(DEP5FilesParagraph([single.path], single.copyright, single.license))
    return dep5_dokument


def convert_dep5_to_calir(dep5_document: DEP5Document, root_path: Path = None) -> CALIR:
    calir = CALIR()
    for files_paragraph in dep5_document.files_paragraphs:
        license = guess_license_expression(files_paragraph.license)
        for glob_pattern in files_paragraph.files:
            for path in expand_dep5_glob(glob_pattern, root_path):
                single = CALIRSingle(path, files_paragraph.copyright, license)
                calir.add_single(single, overwrite=True)
    return calir
