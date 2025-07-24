# Functions have to be defined before use
def function():
    print("Function called")

function()    

# Functions can take arguments and return a value
def sum(x, y):
    return x + y

# Classes and objects (instances)
class MyClass:
    prop = "prop"

    def method(self):
        print("prop")

instance = MyClass()

print(instance.prop)
instance.method()

# class constructor
class AnotherClass:
    def __init__(self, value):
        self.value = value

    def printNumber(self):
        print("Number is %d" % self.value)

another = AnotherClass(77)

another.value = 58

another.printNumber()