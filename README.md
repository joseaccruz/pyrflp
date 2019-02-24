# To Do

- Prepare and test pip install from git.
- Update this README.md (include how to use it and caveats)
- Put all common code in a separate library.
- Read gel graphs settings from a configuration file.
- Generate the gel graphs in SVG for easy of use and customization.
- Improve the LONG_DESCRIPTION on the setup.py file

# Introduction

`PyRFLP` is an experimental tool for easy RFLP (Restriction Fragment Length Polymorphism) analysis. It relies heavily on the excelent `Bio.Restriction` module of the `biopython` packages.

`PyRFLP` started as an original idea of ISPA's professor Frederico Almada and his student Joana Paulas (www.ispa.pt). The current code was developed by Jose Cruz.

## IMPORTANT: Note of Caution

__This is an experimental project!__

This tool was developed to speed up and easy the process of RFLP analysis design and should not replace knowledge, common sense and critical thinking. Please, when using the tool do not blindly rely on the obtained results and __do not acquire restriction enzymes without careful analysis of the results__.



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
$ pip install https://github.com/joseaccruz/pyrflp/archive/master.zip
~~~

The `pip install` command should download and install all depedencies of the tool. To check if everything is working do:

~~~
$ 
~~~

3. Install (with pip) the dependencies:

~~~
biopython==1.70
numpy==1.13.1
Pillow==4.2.1
pkg-resources==0.0.0

ex.:
    (biop)$ pip install biopython
~~~

4. Work on this directory

## Windows

# Restriction Enzymes

For more information about RE read:

- http://biopython.org/DIST/docs/cookbook/Restriction.html