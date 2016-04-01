#####################################
# steganography.py version 0.1      #
# Nick Klose | nick.klose@gmail.com #
#####################################

import os, sys, getopt, imp, ntpath
from PIL import Image
import thread, string, re
from PyQt4 import QtCore, QtGui
from gui_main import Ui_MainWindow

class Steganography(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_process.setEnabled(False)
        
        # initialize variables
        self.imagePath = ""
        self.textPath = ""
        
        self.messageText = ""
        self.messageDefault = "This mode allows you to select an image file and enter a message below. When you are finished, click Process."
        self.messageDecode = "This mode allows you to read a message from an encoded image by entering the correct spacing. When you are ready, click Process."
        self.allowedChars = string.letters + string.digits + "!\"#$%&'()*+-,/:;<=>?@[]^_`{}~"
        self.image = None
        self.encode = True
        
        self.numPixels = 0
        self.spacing = 32
        self.currentChars = 0
        self.maxChars = 0
                
        # disable resizing of the window
        self.setFixedSize(self.size())
        
        # set up aliases for interface object connections
        clicked = QtCore.SIGNAL("clicked()")
        changed = QtCore.SIGNAL("currentChanged()")
        valueChanged = QtCore.SIGNAL("valueChanged(int)")
        toggled = QtCore.SIGNAL("toggled(bool)")
        textChanged = QtCore.SIGNAL("textChanged()")
        
        # button connections
        QtCore.QObject.connect(self.ui.btn_load, clicked, self.loadImage) # load image button
        QtCore.QObject.connect(self.ui.btn_process, clicked, self.process) # process button
        QtCore.QObject.connect(self.ui.btn_load_text_file, clicked, self.loadTextFile) # load text file button
        
        # spin box connection
        QtCore.QObject.connect(self.ui.box_spacing, valueChanged, self.changeSpacing)
        
        # text box connection
        QtCore.QObject.connect(self.ui.text_message, textChanged, self.updateMessage)
        
        # radio button connections
        QtCore.QObject.connect(self.ui.radio_encode, toggled, self.setEncode)
        QtCore.QObject.connect(self.ui.radio_decode, toggled, self.setDecode)
    
    # select an image file to load into the program
    def loadImage(self):
        validImage = True
        
        # open file loader to get image path
        self.imagePath = str(QtGui.QFileDialog.getOpenFileName())
        
        # check if the user canceled the dialog
        if self.imagePath == "" or self.imagePath == None:
            validImage = False
        
        if validImage:
            try:
                rawImage = Image.open(self.imagePath)
                self.image = Image.new("RGB", rawImage.size)
                self.image.paste(rawImage)
            
                self.ui.lbl_image.setPixmap(QtGui.QPixmap(self.imagePath))
                
                self.numPixels = 0
                for pixel in self.image.getdata():
                    self.numPixels += 1
                
                self.message("Image loaded successfully.")
                self.displayImageInfo()
            except Exception as e:
                self.message("Error loading image:\n" + str(e))
    
    # show image-related statistics
    def displayImageInfo(self):
        (width, height) = self.image.size
        self.numPixels = 0
        for pixel in self.image.getdata():
            self.numPixels += 1
        
        self.ui.lbl_height_value.setText(str(height) + " px")
        self.ui.lbl_width_value.setText(str(width) + " px")
        self.ui.lbl_format_value.setText("PNG")
        self.ui.lbl_size_value.setText(str(os.stat(self.imagePath).st_size) + " bytes")
        self.ui.lbl_filename.setText(ntpath.basename(self.imagePath))
        self.maxChars = self.numPixels // self.spacing - 8
        self.updateCharacters()
    
    # display a message for the user
    def message(self, text):
        self.ui.lbl_status.setText(str(text))
        
    # run the encoding/decoding procedure
    def process(self):
        if self.encode:
            self.message("Processing...")
            prefix = str(self.currentChars).zfill(8) # first 8 digits signify length of message
            message = prefix + self.messageText
            pixels = list(self.image.getdata())
            i = 0
            messageIndex = 0
            while i < self.numPixels and messageIndex < len(message):
                if (i % self.spacing) == 0:
                    # set pixel to value of space character
                    pixel = pixels[i] #current pixel
                    red = pixel[0] # red pixel value
                    grn = pixel[1] # green pixel value
                    blu = pixel[2] # blue pixel value
                    
                    # convert values to multiples of 35
                    newRed = red - (red % 35)
                    newGrn = grn - (grn % 35)
                    newBlu = blu - (blu % 35)
                    
                    # get character to encode into pixel
                    char = message[messageIndex]
                    charId = self.id(char)
                    
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
                    self.message(str(messageIndex) + " Adding pixel...")
                    messageIndex += 1
                i += 1
            
            self.message("Finished processing; saving image")
            
            newImage = Image.new("RGB", self.image.size)
            newImage.putdata(pixels)
            
            # ask user to select a save location and filename
            savePath = str(QtGui.QFileDialog.getSaveFileName(this, tr("Save File"), tr("Images (*.png *.jpg *.bmp)")))
            
            # check if the user canceled the dialog
            if savePath == "" or self.imagePath == None:
                self.message("Save cancelled.")
            else:
                try:
                    newImage.save(savePath)
                    self.message("Image saved to " + savePath)
                except Exception as e:
                    self.message("Error saving image:\n" + str(e))
                
        else:
            self.message("Attempting to decode...")
            pixels = list(self.image.getdata())
            i = 0
            message = ""                
                
            while i < self.numPixels:
                if (i % self.spacing) == 0:
                    message += self.pixelToChar(pixels[i])
                i += 1
                
            # find the length of the encoded message
            try:
                messageLength = int(message[:8])
                # trim the garbage data
                maxSize = len(pixels)
                charsToRemove = -1 * (len(message) - messageLength - 8)
                messageBody = message[8:charsToRemove]
                
                # display the decoded message
                self.ui.text_message.setEnabled(True)
                self.ui.text_message.setText(messageBody)
                self.message("Decoding complete.")
            
            # couldn't convert first 8 characters to an int, indicating a problem
            except ValueError:
                self.message("Could not decode; is there a message in this image? If so, is the spacing value correct?")
                
            
            
    # load a message to encode from a text file
    def loadTextFile(self):
        validFile = True
        
        # open file loader to get text file path
        self.textPath = str(QtGui.QFileDialog.getOpenFileName())
        
        # check if the user canceled the dialog
        if self.textPath == "" or self.textPath == None:
            validFile = False
            
        if validFile:
            try:
                # load the text file and display info about it
                textFile = open(self.textPath, 'r')
                self.messageText = str(textFile.read())
                self.ui.text_message.setText(self.messageText)
                self.currentChars = len(self.messageText)
                self.updateCharacters()
            except Exception as e:
                self.message("Error loading text file.\n" + str(e))
    
    # enables encoding mode, which encodes some text into an image
    def setEncode(self):
        self.encode = True
        self.message(self.messageDefault)
        self.ui.text_message.setEnabled(True)
        
    # enables decoding mode, which reads text from an encoded image
    def setDecode(self):
        self.encode = False
        self.message(self.messageDecode)
        self.ui.text_message.setEnabled(False)
        self.ui.text_message.setText("")
    
    # update the interface when the spacing value is changed
    def changeSpacing(self):
        self.spacing = self.ui.box_spacing.value();
        self.displayImageInfo()
        self.updateCharacters()
        
    # update the character count shown below the text box
    def updateCharacters(self):
        self.ui.lbl_max_length_value.setText(str(self.maxChars) + " characters")
        self.ui.lbl_num_characters.setText(str(self.currentChars) + " / " + str(self.maxChars) + " characters")
        
        # message too long
        if self.currentChars > self.maxChars:
            self.ui.lbl_num_characters.setStyleSheet('color: red')
            self.message("Too many characters. Reduce the spacing, shorten your message, or use a larger image.")
            self.ui.btn_process.setEnabled(False)
            
        # message blank
        elif self.currentChars == 0 and self.encode:
            self.message(self.messageDefault)
            self.ui.lbl_num_characters.setStyleSheet('color: black')
            self.ui.btn_process.setEnabled(False)
            
        # message is ok
        else:
            self.ui.lbl_num_characters.setStyleSheet('color: black')
            self.message(self.messageDefault)
            self.ui.btn_process.setEnabled(True)
    
    # update the interface when the text message is modified
    def updateMessage(self):
        # back up the old message in case something goes wrong
        oldMessage = self.messageText;
        try:
            # read message and update the interface
            self.messageText = str(self.ui.text_message.toPlainText())
            self.currentChars = len(self.messageText)
            self.updateCharacters()
        except Exception as e:
            # discard the changes, as they are invalid
            self.message("Invalid character entered.")
            self.messageText = oldMessage
            self.ui.text_message.setText(oldMessage)
    
    # return the numeric ID of a given character
    ## ASCII values between 32 (space [ID=0]) and 126 (~ [ID=94]) are allowed
    ## value 95 represents a newline character
    ## values outside of this range default to space characters
    def id(self, char):
        # get the ASCII value
        asc = ord(char)
        
        # find the ID
        id = asc - 32
        if char == '\n':
            id = 95
        elif id < 0 or id > 94:
            id = 0

        return id

    # return the character corresponding to a given pixel
    def pixelToChar(self, pixel):
        red = pixel[0]
        grn = pixel[1]
        blu = pixel[2]
        charId = (red % 35) + (grn % 35) + (blu % 35)
        if charId == 95:
            return '\n'
        else:
            return chr(charId + 32)


# start in the main function
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = Steganography()
    gui.show()
    sys.exit(app.exec_())
    