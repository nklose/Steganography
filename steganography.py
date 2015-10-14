import os, sys
from PIL import Image

def main():
    
    verbose = True # whether to show debug messages
    numPixels = 0  # total image pixel count
    
    # open the image file
    imageName = getFilename()
    image = Image.open(imageName)

    # count how many pixels it has
    numPixels = 0
    for pixel in image.getdata():
        numPixels += 1
    if (verbose):
        print("Image pixels: " + str(numPixels))

    

    

# finds the length of the longest possible message for a given number of pixels
def getMaxMessageLength( pixels ):
    pixelsPerLetter = 32

    return pixels // 32


# returns the name of a valid image file from the user
def getFilename():
    fileName = None
    validFile = False
    while not validFile:
        try:
            fileName = raw_input("Enter the filename of the image to use: ")
            image = Image.open(fileName)
            image.close()
            validFile = True
        except IOError as e:
            print("Could not open file. Exception: " + str(e))
            print("Please try again.")
            validFile = False
    print("Opening file " + fileName + "...")
    return fileName

if __name__ == '__main__':
    sys.exit(main())
