import os, sys
from PIL import Image

def main():
    imageName = getFilename()
    image = Image.open(imageName)

    numPixels = 0
    for pixel in image.getdata():
        numPixels += 1

    print("Image pixels: " + str(numPixels))


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
