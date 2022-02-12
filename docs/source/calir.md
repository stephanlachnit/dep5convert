<!--
SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# CALIR

> CALIR is an acronym for Copyright And License Intermediate Representation

## Rationale

To convert between the different formats, this module introduces a "intermediate representation" (named CALIR) for the copyright and license information of a file collection on a per-file basis. This is needed since the different formats, namely DEP5 and SPDX, provide copyright and license information in a different way.

The header paragraphs of a DEP5 document can contain metadata not available in SPDX. In addition, DEP5 allows for file globbing, which SPDX does not. An SPDX document can also contain metadata not available in DEP5, most notably file hashes.

To simplify the conversion process, the input format is first converted to CALIR before being converted to the output format. Thus, CALIR only contains the metadata available in both formats. Additional metadata can be specified before converting to the output format. This allows to simplify the problem into smaller steps.

The reset of this section goes into the technical details, which is not essential to read for normal usage of the module.

## Realization

This IR is realized by three main classes:

- {class}`.calir.SinlgeFile` for copyright and license information of a single file
- {class}`.calir.FileCollectionMetadata` for metadata of a file collection
- {class}`.calir.CALIR` for the full copyright and license of a file collection including metadata

Classes for additional metainfo available in SPDX and DEP5 live in the {mod}`.calir.spdx_metadata` and {mod}`.calir.dep5_metadata` modules.

### Information in the {class}`~.calir.SinlgeFile` class

### Information in the {class}`~.calir.FileCollectionMetadata` class
