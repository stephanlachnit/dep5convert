# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Command-line interface for dep5convert module.
"""


import argparse
import logging
import sys

from . import __version__
from .converters import dep5tospdx, spdxtodep5, dep5dump


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
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')

    subparsers = parser.add_subparsers(title='Subcommands', required=True)

    dep5tospdx_help = 'Convert DEP5-style copyright information to SPDX-style'
    parser_dep5tospdx = subparsers.add_parser('dep5tospdx', help=dep5tospdx_help, description=dep5tospdx_help)
    parser_dep5tospdx.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser_dep5tospdx.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser_dep5tospdx.set_defaults(subcmd='dep5tospdx')

    spdxtodep5_help = 'Convert SPDX-style copyright information to DEP5-style'
    parser_spdxtodep5 = subparsers.add_parser('spdxtodep5', help=spdxtodep5_help, description=spdxtodep5_help)
    parser_spdxtodep5.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser_spdxtodep5.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser_spdxtodep5.set_defaults(subcmd='spdxtodep5')

    dep5dump_help = 'Dump information of DEP5-style copyright information'
    parser_dep5dump = subparsers.add_parser('dep5dump', help=dep5dump_help, description=dep5dump_help)
    parser_dep5dump.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser_dep5dump.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    parser_dep5dump.set_defaults(subcmd='dep5dump')

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

    if cli_options.subcmd == 'dep5tospdx':
        dep5tospdx(cli_options.infile, cli_options.outfile)
    elif cli_options.subcmd == 'spdxtodep5':
        spdxtodep5(cli_options.infile, cli_options.outfile)
    elif cli_options.subcmd == 'dep5dump':
        dep5dump(cli_options.infile, cli_options.outfile)

    return 0
