# Introduction

`PyRFLP` is an experimental tool for easy RFLP (Restriction Fragment Length Polymorphism) analysis. It relies heavily on the excelent `Bio.Restriction` module of the `biopython` packages.

__IMPORTANT: Note of Caution - This is an experimental project!__

This tool was developed to speed up and easy the process of RFLP analysis design and should not replace knowledge, common sense and critical thinking. Please, when using the tool do not blindly rely on the obtained results and __do not acquire restriction enzymes without careful analysis of the results__.


# Authorship

`PyRFLP` started as an original idea of ISPA's professor Frederico Almada and his student Joana Paulas (www.ispa.pt). The current code was developed by Jose Cruz.


# Installation

## Linux

Before proceeding make sure you have `Python 3.5` or later installed in you machine. All commands bellow assume that.

### Setup and Activate a Virtual Environment (optional)

Although optional we strongly suggest that you create and activate a virtual environment:

~~~
$ python -m venv <your_env_dir>/ve_rflp
$ source <your_env_dir>/ve_rflp/bin/activate
~~~

If you are not familiar with virtual environments and their benefits check [this](https://realpython.com/python-virtual-environments-a-primer/) nice tutorial.

### Install the tool

Use `pip` to download and install the tool:

~~~
$ pip install git+https://github.com/joseaccruz/pyrflp
~~~

The `pip install` command should download and install all depedencies of the tool. To check if everything is working do:

~~~
$ python -m pyrflp
~~~

The following message should be displayed:

~~~
usage: __main__.py [-h] {lre,lsup,analyse,gel} ...
~~~

## Windows

The tools was note yet tested on `Windows`. We suggest you to install the `Anaconda` package (find it [here](https://www.anaconda.com/distribution/#download-section)) to get `Python 3.7` and `pip` up and running.

After installing Anaconda check the "Linux - Install the tool" section on this README.


# Usage

## Basic Concepts

To use PyRFLP you just have to type `python -m pyrflp` followed by one of the available commands. To obtain a list of all commands type:


~~~
python -m pyrflp --help
~~~

You can use the parameter `--help` to get more information about each individual command. For example, type:

~~~
python -m pyrflp analyse --help
~~~

To get more information about the `analyse` command.


## Simple Analysis

To perform the most simple analysis do:

~~~
python -m pyrflp analyse some_file.fasta
~~~

In which `some_file.fasta` is any valid FASTA file containing DNA sequences.

By default PyRFLP will search the combination of 2 the most common (see the `lres` command) REs that when applied separately to all sequences was the best to distinguish of sequences from each other. The final result will be a list with the best 5 pairs of enzymes.

In the example below we applied the `analysed` command to the sample file that is available in the package (https://github.com/joseaccruz/pyrflp/tree/master/sample):

~~~
FaiI, was (98%)
	 sequences from each other
AfaI, was (96%)
	 sequences from each other
	 M021_klon8c M034_klon2a
Bsa29I, was (96%)
	 sequences from each other
	 M021_klon8a M021_klon21
BseCI, was (96%)
	 sequences from each other
	 M021_klon8a M021_klon21
BshVI, was (96%)
	 sequences from each other
	 M021_klon8a M021_klon21
~~~

This results tell us that the pair of REs "FaiI" and "TaqI", when applied to the 12 sequences of the sample.fasta file, was able to distinguish 98% all pairs of sequences, i.e., these REs allow any of the 12 sequences to be distinguished from any other sequence, except for the sequence "M021_klon8a" from "M021_klon21". The pair "AfaI" and "FaiI" failed to distinguish "M021_klon8a" from "M021_klon21" and "M021_klon8c" from "M034_klon2a".


Notice that you can configure PyRFLP to search the best combination of 3, 4, or any number of REs. Be careful though as testing as many combinations can take a lot of time!

## Simulate the gels

PyRFLP can generate images with the simulation of the DNA gels that result from the digestion of the sequences in the FASTA file by a specific enzyme.

The following command:

~~~
python -m pyrflp gel sample/sample.fasta sample/sample.png FaiI
~~~

Will generate the image that simulates the digestion of the sequences on `sample.fasta` by the RE "FaiI":

![Digestion Gel](https://github.com/joseaccruz/pyrflp/blob/master/sample/sample.png)


# Caveats

This is a work in progress project and is still in it's very early stage. Please be aware of the following caveats:

- The analysis is done one RE at a time, i.e., we don't consider sequential digestions by several REs. If this is an important issue please let us know. 
- This documentation is the bare minimal one. We do not included all commands here. Improved documentation should be made available in the future.
- The whole project was tested with a minimal set of files. Please be ware of potential errors.


# Restriction Enzymes

For more information about RE used in the project please read:

- http://biopython.org/DIST/docs/cookbook/Restriction.html


# To Do

- Prepare and test pip install from git.
- Update this README.md (include how to use it and caveats)
- Put all common code in a separate library.
- Read gel graphs settings from a configuration file.
- Generate the gel graphs in SVG for easy of use and customization.
- Improve the LONG_DESCRIPTION on the setup.py file
- Correct the entry point issues:
	- When displaying errors display __main__.py instead of the correct name.
	- when calling "$ pyrflp" from command line (see: https://github.com/jakubroztocil/httpie for inspiration)


