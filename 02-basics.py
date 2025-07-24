# Boolean checks
x = 2
print(x ==2)
print(x != 2)

# Using "in" 
name = "William"

if name in ["William", "Costa"]:
    print("Name is in the list")

# Identation
if name == "William":
    print("Line 1")
    print("Line 2")

# if - else if - else
if name == "William":
    print("if Line 1")
    print("if Line 2")
elif name != "Costa":
    print("elif Line 1")
else:
    print("else Line 1")

# Note falsy values: "", [], 0, False

# "is" test object instances
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False    

# Use not to switch the boolean expression
print(not False) # Prints out True

# "for" loops can use range objects
# syntax: range(start, stop, step)
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# "while" loops
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# Note you can use break and continue as well inside loops

# you can use else in loops to execute when for or while conditions fails
count = 0

while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
# Break finishes loop, 
# continue stops current iteration and starts next
# else when "for" condition returns false
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")