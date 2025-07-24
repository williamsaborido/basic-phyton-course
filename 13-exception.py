# You can use try/except just as another languages
def printNum(integer):
    print(f"Number is {integer}")

def process():
    numList = [1, 2, 3, 4, 5]

    
    try:
        for index in range(10):
            printNum(numList[index])
        # You can catch the exception by type
    except IndexError as e:
        print(f"Error: {e}. Execution ended.")

process()