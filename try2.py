while True:    # here the loop is added untill the vlue is an int
    try:
        x = int(input("Enter the vaule of x: "))
    except ValueError:
        print("the value is not an integer")
    else:
        break     # here the else condition breaks the loop once the value is int and prints the condition down.

print(f"The value of x is {x}")

# Can be also written as

while True: 
    try:
        x = int(input("Enter the vaule of x: "))
        break          # here the value breaks once we got an integer
    except ValueError:
        print("the value is not an integer")

print(f"The value of x is {x}")