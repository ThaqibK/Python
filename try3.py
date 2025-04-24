def main1():   # defining the function 
    x = get_int()
    print ((f"The value of x is {x}"))

def get_int():
    while True: 
        try:
            x = int(input("Enter the vaule of x: "))
        except ValueError:
            print("the value is not an integer")
        else:
            break
    return x

main1()

# Can be also written as

def main2():
    x = get_int()
    print ((f"The value of x is {x}"))

def get_int():
    while True: 
        try:
            x = int(input("Enter the vaule of x: "))
        except ValueError:
            print("the value is not an integer")
        else:
            return x

main2()

# Can be also written as

def main3():
    x = get_int()
    print ((f"The value of x is {x}"))

def get_int():
    while True: 
        try:
            x = int(input("Enter the vaule of x: "))
            return x
        except ValueError:
            print("the value is not an integer")

main3()

# Can be also written as

def main4():
    x = get_int()
    print ((f"The value of x is {x}"))

def get_int():
    while True: 
        try:
            return int(input("Enter the vaule of x: "))
        except ValueError:
            print("the value is not an integer")

main4()

# Can also be written as

def main5():
    x = get_int()
    print ((f"The value of x is {x}"))

def get_int():
    while True: 
        try:
            x = int(input("Enter the vaule of x: "))
            return x
        except ValueError:
            pass     # This pass statement just pass the error. Instead of writing any sentences it just passes and continues the loop.

main5()

# Can be also written as

def main6():
    x = get_int("Enter the value of x: ")  # the question is asked here. The input will be called at the below definition
    print ((f"The value of x is {x}"))

def get_int(prompt): # the caller is named as prompt
    while True: 
        try:
            x = int(input(prompt))  # same it is called here for input
            return x
        except ValueError:
            pass 

main6()