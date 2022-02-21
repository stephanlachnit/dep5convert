# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains helper function for dep5_tools.
"""


from pathlib import Path

from .classes import DEP5Document


def expand_dep5_glob(glob_pattern: str, source_path: Path) -> list[Path]:
    pass


def add_license_paragraphs(dep5_document: DEP5Document) -> DEP5Document:
    return dep5_document


def guess_license_expression(license_str: str) -> str:
    return license_str
