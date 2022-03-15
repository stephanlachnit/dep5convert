# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Contains helper function for dep5_tools.
"""


import os
from pathlib import Path
import re


def expand_rfc822_lists(string: str) -> list[str]:
    # TODO
    return list[str]([string])


def expand_dep5_glob(glob_pattern: str, source_path: Path) -> list[Path]:

    # Convert glob pattern to regex
    regex_glob_pattern = str()
    glob_pattern_chars = list(glob_pattern)
    it_glob_pattern_chars = enumerate(glob_pattern_chars)
    for count, char in it_glob_pattern_chars:
        if char == '\\':
            if glob_pattern_chars[count + 1] == ['*', '?', '\\']:
                regex_glob_pattern += glob_pattern_chars[count + 1]
                try:
                    next(it_glob_pattern_chars)
                except StopIteration as error:
                    raise Exception('Glob pattern end with "\\"') from error
            else:
                raise Exception(f'"{glob_pattern_chars[count + 1]}" is not allowed after "\\"')
        else:
            regex_glob_pattern += re.escape(char)

    # add source path to glob pattern
    regex_source_path = re.escape(source_path.resolve().as_posix() + os.path.pathsep)
    regex_full_glob_pattern = regex_source_path + regex_glob_pattern

    # walk through source path and match files
    for dirpath, _dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            path = os.path.abspath(os.path.join(dirpath, filename))
            if re.match(regex_full_glob_pattern, path):
                yield path


def guess_license_expression(license_str: str) -> str:
    return license_str
