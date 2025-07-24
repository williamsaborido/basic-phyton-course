# Hello world
print("Hello world")

# Arithmetic, int and floats, var definitions
vBc, pIcms = 1575, 18
vIcms = float(0)
vIcms = (vBc / 100) * pIcms

# power
print("3 powers 3: %d" % 3 ** 3)

# repeat a string n times
print(" repeat " * 10)

# print() output and formatting
print("Tax added: " + str(vIcms)) #string
print("Calc base: %f" % vBc) #float
print("Hex: %x and %X" % (748, 17589)) #hex and HEX
print("Total: %.3f, tax: %.2f" % (vIcms, pIcms)) #float w/ decimal places
print("Name: %s" % "William") #string

# Array/list
fileList = []
fileList.append("test.txt")
fileList.append("movie.mp4")
fileList.append("music.mp3")
fileList.append("document.pdf")
fileList.append("program.exe")
fileList.append("link.url")

# Iterating array/list
for file in fileList:
    print(file)

# Print as array
print(fileList)

scriptsList = ["main.py", "math.py", "string.py"]

# Merge arrays
print(fileList + scriptsList)
print(scriptsList * 2)

# You can print as string too
print("List: %s" % scriptsList)

# String indexing and count
text = "error code: 2541 - File not found"
print(text.index("-"))
print(text.count("o"))

# Substring
print(text[3])
print(text[0:4])
print(text[4:5])

# extended notation [start:stop:step]
print(text[0:13:2])

# Reverse string
print(text[::-1])

# String casing
print(text.upper())
print(text.lower())

# Test if substring exists
print(text.startswith("error"))
print(text.endswith("William"))

# Split string to string list discarding the separator
fields = "name;age;city;salary"
for field in fields.split(";"):
    print(field)

