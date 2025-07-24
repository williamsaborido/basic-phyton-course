# Read a string from the user and print it
inputStr = input("Enter a string: ")
print("You entered: %s" % inputStr)

input("Enter")

# Converting input
inputInt = int(input("Enter an integer: "))
decInput = float(input("Enter a decimal number: "))
print("You entered integer: %d and decimal: %.2f" % (inputInt, decInput))

# Reading multiple inputs in one line
inputList = input("Enter multiple values separated by space: ").split()
print("You entered: ", inputList)

# You can use map to convert the list of strings to integers
sum = 0
for i in map(int, inputList):
    sum += int(i)
print("Sum of the integers you entered: %d" % sum)