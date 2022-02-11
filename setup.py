#!/usr/bin/python3

# SPDX-FileCopyrightText: 2022 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: CC0-1.0

"""
Install script for dep5convert.
"""


import setuptools


if __name__ == '__main__':
    with open('README.md', 'rt', encoding='utf-8') as readme_file:
        long_description = readme_file.read()

    setuptools.setup(
        name='dep5convert',
        version='0.0.0',
        author='Stephan Lachnit',
        author_email='stephanlachnit@debian.org',
        description='module for converting DEP5-style copyright files',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/stephanlachnit/dep5convert',
        project_urls={
            'Source': 'https://github.com/stephanlachnit/dep5convert',
            'Bug Tracker': 'https://github.com/stephanlachnit/dep5convert/issues',
        },
        classifiers=[
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
        ],
        python_requires='>=3.9',
        package_dir={'': 'src'},
        packages=setuptools.find_packages(where='src'),
        entry_points={'console_scripts': ['dep5convert = dep5convert.cli:main']},
    )
