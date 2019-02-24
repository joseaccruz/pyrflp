#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import io
#import os
#import sys
#from shutil import rmtree

from setuptools import setup

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
    version="0.0.1",
    author="Jose Cruz",
    author_email="joseaccruz@gmail.com",
    description="Tool for easy Restriction fragment length polymorphism analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joseaccruz/pyrflp",
    python_requires=">=3.5.0",
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
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

