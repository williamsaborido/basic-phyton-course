# Fibonacci generator function 
# (it yelds Fibonacci numbers indefinitely while the iterator keeps asking the next value)
def fib():
    n1 = 1
    n2 = 1

    while True:
        yield n1
        n1, n2 = n2, n1 + n2
        # to invert the order, use: # n1, n2 = n2, n1 


# testing code
import types

if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0

    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

# Testing fibonacci regular function
def fibonacci(count):
    n1 = 0
    n2 = 1
    res = 0
    
    for i in range(count):
        
        if i <= 0:
            res = 1
        else:
            res = n1 + n2
            n1 = n2
            n2 = res       
        
        print("%d. %d" % (i + 1, res))              

    return (res, i + 1)

result = fibonacci(10)
print("Fibonacci sequence: %i in %i loops" % result)