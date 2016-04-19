# Image Steganography Project (version 1.0)
Copyright © 2015 [Nick Klose](http://ualberta.ca/~klose) under the GNU General Public License, Version 2.

This software is a personal [steganography](http://en.wikipedia.org/wiki/Steganography) project, which encodes alphanumeric messages in regular images. The messages are encoded by making slight modifications to the colour values of specific pixels. A single pixel can encode a single character, and the selected "spacing" value determines how many pixels are skipped before the next character is encoded. The messages can then be decrypted by a recipient using the same software, as long as the recipient knows what pixel spacing was used in the original encoding.

## Included Files
* sample.jpg is a free image from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Peyto_Lake-Banff_NP-Canada.jpg)

## Usage

On Windows, simply open `Steganography.exe` to use the software.

To run the program through Python on Windows or another platform, you will need to install the software's dependencies separately. See the Required Packages section for more info on this.

### Encoding
1. Open the program
2. Click *Load Image*, then select a valid image file to encode your message into. Any PIL-supported image should work.
3. Type your message into the text box at the bottom, or use the *Load Text File* button to use an existing text file. The file extension is ignored.
4. Select the *Spacing* value using the spin box at the top-left. This determines how many pixels are skipped before encoding the next pixel. Note that an 8-character prefix will automatically be appended to your message, which marks how long the message is.
5. Verify that the message will fit into your selected image. If it doesn't fit, you will need to (a) use an image with more pixels, (b) lower your spacing value, or (c) shorten your message.
6. Click *Process*, then select the location and name for your encoded image.

### Decoding
1. Select the *Decode Image* radio button at the top-left.
2. Click *Load Image*, then select your encoded image.
3. Set the *Spacing* value to the same number used in the original encoding.
3. Click *Process*. The encoded message will appear in the text box at the bottom.

## Required Packages

[Python 2.7](https://www.python.org/) (32-bit) is required to run this software. 

The software requires either `PIL` (Copyright © 1997-2011 by Secret Labs AB & Fredrik Lundh) or `Pillow` (Copyright (c) 1995-2015 Fredrik Lundh and Contributors, Alex Clark and Contributors).

The GUI version of the software also requires `PyQt4` for Python 2.7, which is Copyright © 2015 Riverbank Computing Limited.

### Windows
* [`Python` Download](htts://python.org/downloads)
* [`PIL` Download](http://www.pythonware.com/products/pil/#pil117)
* [`PyQt4` Download](https://www.riverbankcomputing.com/software/pyqt/download)

### Ubuntu

Follow these instructions to install the required packages:

1. Run `sudo apt-get update` to get the latest package lists
2. Install `pip` and `PyQt4` with `sudo apt-get install python-pip python-qt4`
3. Install other required packages with `apt-get build-dep python-imaging libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev`
4. Install Pillow with `pip install Pillow`
