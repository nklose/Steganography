filename = ""
try:
    filename = str(input("Enter a filename to import: "))
except Exception as e:
    print("Error: " + str(e))
    
print("Opening " + filename)
