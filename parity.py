def main():
    x = int(input("Enter the vaule of x: "))
    if is_even(x):
        print ("x is an even number")
    else:
        print ("x is an odd number")

def is_even(n):
    return n % 2 == 0  # This return value checks if the number is true. If its true it passes the return value.

main()

'''
also writen as

def is_even(n):
    return True if n % 2 == 0 else False

or

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

'''