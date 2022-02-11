# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Command-line interface for dep5convert module.
"""


import argparse
import logging
import sys

from . import _VERSION


def parse_args(args: list[str]) -> argparse.Namespace:
    """
    Parses the command-line arguments.

    Args:
        args: List of strings to parse as command-line arguments.
    Returns:
        A namespace with the parsed arguments.
    """

    parser = argparse.ArgumentParser(description='tool for converting DEP5-style copyright files')

    parser.add_argument('-v', '--verbose', help='enable verbose output', action='store_true')
    parser.add_argument('--version', action='version', version=f'%(prog)s {_VERSION}')

    return parser.parse_args(args=args)


def main(args: list[str] = None) -> int:
    """
    Runs the command-line interace.

    Args:
        args: List of strings to parse as command-line arguments. Defaults to sys.argv if set to None.
    Returns:
        Int with return code.
    """

    logging.basicConfig(level=logging.INFO, format='%(message)s')

    if args is None:
        args = sys.argv[1:]

    cli_options = parse_args(args)

    if cli_options.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug('Running with verbose output')

    return 0
