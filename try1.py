try:        # this is used for error handling
    x = int(input("Enter the vaule of x: "))
    print(f"value of x is {x}")
except ValueError:  # valueError is if string is passed instead of int or any other. Other than the mentioned.
    print("the value is not an integer")

# New problem

try:
    x = int(input("Enter the vaule of x: "))
except ValueError:
    print("the value is not an integer")
else:
    print(f"value of x is {x}")