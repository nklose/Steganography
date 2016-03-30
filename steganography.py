#####################################
# steganography.py version 0.1		#
# Nick Klose | nick.klose@gmail.com #
#####################################

import os, sys, getopt, imp, ntpath
from PIL import Image
import thread
from PyQt4 import QtCore, QtGui
from gui_main import Ui_MainWindow

class Steganography(QtGui.QMainWindow):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		# initialize variables
		self.imagePath = ""
		self.textPath = ""
		self.messageText = ""
		self.messageDefault = "This mode allows you to select an image file and enter a message below. When you are finished, click Process."
		self.messageDecode = "This mode allows you to read a message from an encoded image by entering the correct spacing. When you are ready, click Process."
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
				
				self.message("Image loaded successfully.")
				self.displayImageInfo()
			except Exception as e:
				self.message("Error loading image:\n" + str(e))
			
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
	
	def message(self, text):
		self.ui.lbl_status.setText(str(text))
		
			
	def process(self):
		self.message("Processing...")
		prefix = str(self.currentChars).zfill(8) # first 8 digits signify length of message
		message = prefix + self.messageText
		pixels = list(self.image.getdata())
		i = 0
		messageIndex = 0
		while i < self.numPixels and messageIndex < len(self.messageText):
			if (i % self.spacing) == 0:
				# set pixel to value of space character
				pixel = pixels[i] #current pixel
				red = pixel[0] # red pixel value
				grn = pixel[1] # green pixel value
				blu = pixel[2] # blue pixel value
				
				newRed = red - (red % 35)
				newGrn = grn - (grn % 35)
				newBlu = blu - (blu % 35)
				
				# get character to encode into pixel
				char = self.messageText[messageIndex]
				charId = id(char)
				
				# add a third of the character ID to each color channel
				newRed += (charId // 3) + (charId % 3)
				newGrn += charId // 32
				newBlu += charId // 32
				
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
		
		newImage = Image.new("RGB", self.image.size)
		newImage.putData(pixels)
		
		newImage.save("output.png")
		self.message("Image saved as output.png")
		
	def loadTextFile(self):
		validFile = True
		
		# open file loader to get text file path
		self.textPath = str(QtGui.QFileDialog.getOpenFileName())
		
		# check if the user canceled the dialog
		if self.textPath == "" or self.textPath == None:
			validFile = False
			
		if validFile:
			try:
				textFile = open(self.textPath, 'r')
				self.messageText = str(textFile.read())
				self.ui.text_message.setText(self.messageText)
				self.currentChars = len(self.messageText)
				self.updateCharacters()
			except Exception as e:
				self.message("Error loading text file.\n" + str(e))
	
	# enables encoding mode (radio button)
	def setEncode(self):
		self.encode = True
		self.message(self.messageDefault)
		self.ui.text_message.setEnabled(True)
		
	# enables decoding mode (radio button)
	def setDecode(self):
		self.decode = True
		self.message(self.messageDecode)
		self.ui.text_message.setEnabled(False)
		
	def changeSpacing(self):
		self.spacing = self.ui.box_spacing.value();
		self.displayImageInfo()
		self.updateCharacters()
		
	# update the character count shown below the text box
	def updateCharacters(self):
		self.ui.lbl_max_length_value.setText(str(self.maxChars) + " characters")
		self.ui.lbl_num_characters.setText(str(self.currentChars) + " / " + str(self.maxChars) + " characters")
		if self.currentChars > self.maxChars:
			self.ui.lbl_num_characters.setStyleSheet('color: red')
			self.message("Too many characters. Reduce the spacing, shorten your message, or use a larger image.")
			self.ui.btn_process.setEnabled(False)
		else:
			self.ui.lbl_num_characters.setStyleSheet('color: black')
			self.message(self.messageDefault)
			self.ui.btn_process.setEnabled(True)
	
	def updateMessage(self):
		self.messageText = str(self.ui.text_message.toPlainText())
		self.currentChars = len(self.messageText)
		self.updateCharacters()
		
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
				image.close()
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
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	gui = Steganography()
	gui.show()
	sys.exit(app.exec_())
	