# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
End-to-end converters in the dep5convert module.
"""


from io import TextIOBase, StringIO
from pathlib import Path

from .dep5_tools.convert_text import parse_dep5
from .dep5_tools.convert_calir import convert_dep5_to_calir


def dep5tospdx(infile: TextIOBase, outfile: TextIOBase, source_path: Path = None) -> None:
    dep5_document = parse_dep5(infile)
    calir = convert_dep5_to_calir(dep5_document, source_path)
    print(calir)


def spdxtodep5(infile: TextIOBase, outfile: TextIOBase) -> None:
    print('called spdxtodep5')


def dep5dump(infile: TextIOBase, outfile: TextIOBase, source_path: Path = None) -> None:
    dep5_document = parse_dep5(infile)
    calir = convert_dep5_to_calir(dep5_document, source_path)

    for single in calir.singles:
        outfile.write(f'{single.path} {single.copyright} {single.license}\n')
