#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import io
#import os
#import sys
#from shutil import rmtree

from setuptools import setup

NAME = 'pyrflp'
DESCRIPTION = 'Tool for easy Restriction fragment length polymorphism analysis.'
URL = 'https://github.com/me/myproject'
EMAIL = 'joseaccruz@gmail.com'
AUTHOR = 'Jose Cruz'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = "0.0.1"

REQUIRED = [
    "biopython",
	"numpy",
	"Pillow",
	"scipy",
	"tqdm"
]

# Optional packages
EXTRAS = {}

DESCRIPTION_LONG = """Tool for easy Restriction fragment length polymorphism analysis."""



setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION_LONG,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
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

