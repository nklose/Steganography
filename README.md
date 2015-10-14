# Image Steganography Project
Copyright (c) 2015 Nick Klose under the GNU General Public License, Version 2.

This software is a personal [steganography](http://en.wikipedia.org/wiki/Steganography) project, which encodes alphanumeric messages in regular images. The messages can then be decrypted by a recipient using the same software.

## Features in Development
* Hide alphanumeric messages within a selected image of sufficient resolution
* Messages between two parties can be hidden/revealed using this software and an agreed-upon key
* Support for multiple image formats
* GUI

## Included Files
* sample.jpg is a free image from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Peyto_Lake-Banff_NP-Canada.jpg)

## Required Packages

This software requires `Pillow`, which is Copyright (c) 1995-2015, Fredrik Lundh and Contributors, Alex Clark and Contributors.

The following instructions will install Pillow on Ubuntu 15.04:

# Install pip with `sudo apt-get install python-pip`
# Install the required packages with `apt-get build-dep python-imaging libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev`
# Install Pillow with `pip install Pillow`
