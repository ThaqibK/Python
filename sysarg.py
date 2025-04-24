import sys

if len(sys.argv) < 2:                  #here we eliminated else function which induces index error. To resolve it we are usinf sys.exit
    sys.exit("Too few arguments")      #sys.exit module exits the terminal once the statement is given.
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])

'''
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])
'''

'''
try:                                        # Here we are handling error
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Enter the value at the end.")
'''

'''
print("Hello, my name is", sys.argv[1])  # here the sys.argv replaces the value we enter at the terminal
'''
