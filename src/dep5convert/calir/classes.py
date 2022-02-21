# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

"""
Classes for the Copyright And License Intermediate Representation (CALIR).
"""

from pathlib import Path


class CALIRSingle:
    """
    CALIR for a single file.
    """
    def __init__(self,
                 path: Path,
                 copyright: list[str],
                 license: str,
                 ) -> None:
        self._path = path
        self._copyright = copyright
        self._license = license

    @property
    def path(self) -> Path:
        """
        The path of the file.
        """
        return self._path

    @property
    def copyright(self) -> list[str]:
        """
        The copyright texts applying to the file.
        """
        return self._copyright

    @property
    def license(self) -> str:
        """
        The license expression applying to the file.
        """
        return self._license


class CALIR:
    """
    CALIR for a file collection.
    """
    def __init__(self) -> None:
        self._singles = list[CALIRSingle]()

    @property
    def singles(self) -> list[CALIRSingle]:
        """
        List of included :class:`CALIRSingle` objects.
        """
        return self._singles

    def find_single(self, path: Path) -> CALIRSingle:
        """
        Finds the :class:`CALIRSingle` object for a given path.

        Args:
            path: Path of the file.

        Returns:
            :class:`CALIRSingle` object corresponding to the file for the given path.

        Raises:
            LookupError: if no :class:`CALIRSingle` object is found for the given path.
        """
        for single in self._singles:
            if single.path.samefile(path):
                return single
        raise LookupError(f'Could not find a single correspoding to {path.name}')

    def add_single(self, single: CALIRSingle, overwrite: bool = False) -> None:
        """
        Adds a :class:`CALIRSingle` object to the class.

        Args:
            single: :class:`CALIRSingle` object to add.
            overwrite: If :obj:`True`, overwrite an existing :class:`CALIRSingle` object with the path.

        Raises:
            FileExistsError: If :paramref:`~CALIR.add_single.overwrite` is :obj:`False` and a :class:`CALIRSingle`
                object with the same path already exists.
        """
        for index, single_ in enumerate(self._singles):
            if single.path.samefile(single_.path):
                if overwrite:
                    self._singles[index] = single
                    return
                raise FileExistsError(f'A single already exists with the path {single.path.name}')
        self._singles.append(single)
