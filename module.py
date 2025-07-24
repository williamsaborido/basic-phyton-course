# module.py
# will print some random stuff

def showMessage():
    print("module prints a number: %d" % 42)
    print("end print function")

class MyModule:

    value = 0

    def __init__(self):
        if self.value == 0:
            self.value = 42
        print("module class init with value %d" % self.value)
