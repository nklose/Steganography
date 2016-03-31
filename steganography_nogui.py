# steganography_nogui.py beta v0.1
# run with --help for options

import os, sys, getopt
from PIL import Image

def main(argv):
    
    verbose = False  # whether to show debug messages
    numPixels = 0    # total image pixel count
    imageName = None # filename of the image
    message = ""   # the message to be sent
    density = 32     # how many pixels between those that are modified
    decode = False

    # handle command line arguments
    opts, args = getopt.getopt(argv, "vdei:m:",["help","encode","decode","verbose"])
    for opt, arg in opts:
        if opt == '-v' or opt == '--verbose': # enable verbose mode
            verbose = True
            print("Enabling verbose mode. Remove -v to disable.")
        elif opt == "-i": # specify an input image
            imageName = arg
            try:
                image = Image.open(imageName)
                #image.close()
                if (verbose):
                    print("Input image specified: " + imageName)
            except IOError as e:
                print("Could not open file. Exception: " + str(e))
                imageName = getFilename()
        elif opt == "-m": # specify a message to use
            message = arg
            if (verbose):
                print("Message: " + message)
        elif opt == "--decode" or opt == "-d":
            decode = True
        elif opt == "--help":
            print("steganography.py beta v0.1")
            print("You can add any of the following options while running this from command line:")
            print("\t-i <input image> specifies an image file to load")
            print("\t-v enables verbose mode, printing more details to the console")
            sys.exit()

    

    # open the image file
    if imageName == None:
        imageName = getFilename()
    rawImage = Image.open(imageName)
    image = Image.new("RGB", rawImage.size)
    image.paste(rawImage)

    # count how many pixels it has
    numPixels = 0
    for pixel in image.getdata():
        numPixels += 1
    if (verbose):
        print("Image pixels: " + str(numPixels))

    if not decode:
        # calculate max message length
        maxLength = numPixels // density - 8

        # get and verify the message
        if message == "":
            message = getMessage(maxLength)
        elif len(message) > maxLength:
            print("Specified message is too long for this image. Please enter a shorter one.")
            message = getMessage(maxLength)

        if (verbose):
            print("Encoding message: " + message)

        # encode the message
        messageLength = len(message)
        if (verbose):
            print("Message to encode is " + str(messageLength) + " characters long.")
        prefix = str(messageLength).zfill(8) # the first 8 digits of the message specify the message's length
        message = prefix + message
        print("Message set to " + message)
        if (verbose):
            print("Prefix string is " + prefix)
        pixels = list(image.getdata())
        i = 0
        messageIndex = 0
        while i < self.numPixels and messageIndex < len(message):
            # modify every nth pixel
            if (i % density) == 0:
                # set pixel to "space" value
                pixel = pixels[i] # current pixel
                red = pixel[0] # red pixel value
                grn = pixel[1] # green pixel value
                blu = pixel[2] # blue pixel value

                newRed = red - (red % 35)
                newGrn = grn - (grn % 35)
                newBlu = blu - (blu % 35)

                # get character to encode into this pixel
                char = message[messageIndex]
                charId = id(char)

                # add a third of the character ID to each color channel
                newRed += (charId // 3) + (charId % 3)
                newGrn += charId // 3
                newBlu += charId // 3

                # ensure pixel values are still in range
                if newRed > 255:
                    newRed -= 35
                if newGrn > 255:
                    newGrn -= 35
                if newBlu > 255:
                    newBlu -= 35

                # update the pixel
                newPixel = (newRed, newGrn, newBlu)
                pixels[i] = newPixel

                # check if the character was encoded correctly
                if (verbose):
                    print("Encoded pixel with character " + pixelToChar(newPixel))

                messageIndex += 1
            i += 1
    
        newImage = Image.new("RGB", image.size)
        newImage.putdata(pixels)

        if (verbose):
            print("Outputting modified image as output.png...")
        newImage.save("output.png")

    # decode an image and return the hidden message
    else:
        if message != "":
            print("Warning: both an input message and decoding mode were specified. Discarding message.")
            message = ""
        
        pixels = list(image.getdata())
        i = 0
        while i < numPixels:
            if (i % density) == 0:
                message += pixelToChar(pixels[i])
            i += 1

        # find the length of the encoded message
        messageLength = int(message[:8])
        if (verbose):
            print("Length of encoded message is " + str(messageLength) + " characters.")

        # trim the garbage data from the message string
        maxSize = len(pixels)
        if (verbose):
            print("Max message size is " + str(maxSize))
        charsToRemove = -1 * (len(message) - messageLength - 8)
        messageBody = message[8:charsToRemove]

        # output the final message
        print("Message: " + messageBody)

# get a valid message from the user
def getMessage(maxLength):
    message = raw_input("Enter a message. Max length is " + str(maxLength) + " characters: ")
    while len(message) > maxLength:
        message = raw_input("Message too long. Please try again: ")
    return message

# gets a valid image file from the user
def getFilename():
    fileName = None
    validFile = False
    while not validFile:
        try:
            fileName = raw_input("Enter the filename of the image to use: ")
            image = Image.open(fileName)
            #image.close()
            validFile = True
        except IOError as e: # a wild input error appeared!
            print("Could not open file. Exception: " + str(e))
            print("Please try again.")
            validFile = False
    print("Opening file " + fileName + "...")
    return fileName

# return the ID of a given character
# ASCII values between 32 (space [ID=0]) and 126 (~ [ID=94]) are allowed
# value 95 represents a newline character
# values outside of this range default to space characters
def id(char):
    # get the ASCII value
    asc = ord(char)
    
    # find the ID
    id = asc - 32
    if char == '\n':
        id = 95
    elif id < 0 or id > 94:
        id = 0

    return id

# take a pixel and return the corresponding character
def pixelToChar(pixel):
    red = pixel[0]
    grn = pixel[1]
    blu = pixel[2]
    charId = (red % 35) + (grn % 35) + (blu % 35)
    if charId == 95:
        return '\n'
    else:
        return chr(charId + 32)


# start in the main function
if __name__ == '__main__':
    main(sys.argv[1:])
