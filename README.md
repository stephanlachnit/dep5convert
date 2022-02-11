<!--
SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# dep5convert

[![CI](https://github.com/stephanlachnit/dep5convert/actions/workflows/ci.yaml/badge.svg)](https://github.com/stephanlachnit/dep5convert/actions/workflows/ci.yaml)
[![REUSE status](https://api.reuse.software/badge/github.com/stephanlachnit/dep5convert)](https://api.reuse.software/info/github.com/stephanlachnit/dep5convert)

> dep5convert is a Python module for converting DEP5-style copyright files

## Background

The goal of this project is provide interoperability between Debian's [Machine-readable debian/copyright file](https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/) (abbreviated DEP5 in the following) and the [REUSE](https://reuse.software/spec/) and the [SPDX](https://spdx.github.io/spdx-spec/) specifications. This includes three tasks:

1. Convert from SPDX to DEP5
2. Convert from DEP5 to SPDX
3. Convert from DEP5 to the [new REUSE.yaml format](https://github.com/fsfe/reuse-docs/issues/81)

The first one is to allow the usage of the information REUSE provides to automatically create the DEP5 copyright file for Debian's packages (see [here](https://lists.debian.org/debian-devel/2022/01/msg00309.html)).
The second one is for the same purpose, but aimed at a transition from DEP5 to SPDX as end-user format. Note that the [`reuse-tool`](https://github.com/fsfe/reuse-tool) in its current form already does this.

However, the plan is to move from `DEP5` to a new YAML-based format, where this library could become handy. Eventually, there will be two code paths in this library: `SPDX->DEP5` and `DEP5->REUSE.yaml`. For `DEP5->SPDX`, `DEP5->REUSE.yaml` and the [`reuse`](https://pypi.org/project/reuse/) module will be used.

## Development

Note: this project is currently in planning and is not usable yet. Branches can be subject to force-pushes.

Before you can run the code from source, you first need to run `make`, else you will get a `DistributionNotFound` error. Note that the Makefile is only intended for development use and not for building or installing the module.

To access the CLI:
```sh
make egg_info
cd src
python3 -m dep5convert --help
```

## License

The library code is licensed under the [EUPL-1.2](LICENSES/EUPL-1.2.txt).
The documentation is licensed under [CC-BY-SA-4.0](LICENSES/CC-BY-SA-4.0.txt).
Configuration files are licensed under [CC0-1.0](LICENSES/CC0-1.0.txt).

This repository follows the [REUSE specification](https://reuse.software/spec/). For a comprehensive copyright and license report, you can install the [`reuse-tool`](https://github.com/fsfe/reuse-tool/blob/master/README.md#install) and run `reuse spdx`.
