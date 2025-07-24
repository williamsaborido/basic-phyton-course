# asterisk define the argument is a list
def process(x, y, *args):
    print(f"x: {x}, y: {y}, args: {list(args)}")

process(1, 2, 3, 4, 5)

# double asterisk define the argument is a dictionary
def math(x, y, **args):
    if args.get("operation") == "add":
        return x + y
    elif args.get("operation") == "sub":
        return x - y
    elif args.get("operation") == "mul":
        return x * y
    elif args.get("operation") == "div":
        return x / y
    
    return 0

# you can name variable args to be retrieved by name inside the function
result = math(10, 5, operation="add")

# f allows string interpolation
print(f"Result of addition: {result}")