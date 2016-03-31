# Image Steganography Project
Copyright (c) 2015 Nick Klose under the GNU General Public License, Version 2.

This software is a personal [steganography](http://en.wikipedia.org/wiki/Steganography) project, which encodes alphanumeric messages in regular images. The messages can then be decrypted by a recipient using the same software.

## Included Files
* sample.jpg is a free image from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Peyto_Lake-Banff_NP-Canada.jpg)

## Required Packages

[Python 2.7](https://www.python.org/) is required to run this software. 

The software requires either `PIL` (Copyright © 1997-2011 by Secret Labs AB & Fredrik Lundh) or `Pillow` (Copyright (c) 1995-2015 Fredrik Lundh and Contributors, Alex Clark and Contributors).

The GUI version of the software also requires `PyQt4` for Python 2.7, which is Copyright (c) 2015 Riverbank Computing Limited.

### Windows
* [`PIL` Download](http://www.pythonware.com/products/pil/#pil117)
* [`PyQt4` Download](https://www.riverbankcomputing.com/software/pyqt/download)

### Ubuntu

Follow these instructions to install the required packages:

1. Run `sudo apt-get update` to get the latest package lists
2. Install `pip` and `PyQt4` with `sudo apt-get install python-pip python-qt4`
3. Install other required packages with `apt-get build-dep python-imaging libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev`
4. Install Pillow with `pip install Pillow`
