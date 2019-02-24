#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import pyrflp

REQUIRES_PYTHON = ''

REQUIRED = [
    "biopython",
	"numpy",
	"Pillow",
	"scipy",
	"tqdm"
]

# Optional packages
EXTRAS = {}

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyrflp",
    version=pyrflp.__version__,
    description=pyrflp.__doc__.strip(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joseaccruz/pyrflp",
    download_url="https://github.com/joseaccruz/pyrflp",
    author=pyrflp.__author__,
    author_email="joseaccruz@gmail.com",
    license=pyrflp.__license__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyrflp = pyrflp.__main__',
        ],
    },
    python_requires=">=3.5.0",
    
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Environment :: Console",
		"Intended Audience :: Education",
		"Intended Audience :: Healthcare Industry",
		"Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ]
)

