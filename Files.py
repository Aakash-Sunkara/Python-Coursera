fname = input("Enter the file name:")
file = open(fname, encoding='cp1252')
#for lx in file:
#    ly = lx.rstrip()   # Alternate method to print the data
#    print(ly.upper())
data = file.read()
print(file)   # This is used to know the configuration of the text
print(data.upper())     # upper is used to convert all letters to uppercase
