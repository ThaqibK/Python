def main1():
    print_column(3)

def print_column(height):
    for i in range(height):
        print("#")

main1()

#  New problem

def main2():
    print_row(4)

def print_row(width):
    print("#" * width)

main2()

# New problem

def main3():
    print_square(3)

def print_square(size):
    for i in range(size):    # i represents row
        for j in range(size): # j represents column
            print("#", end="")   # end is used to end the line after the loop ends 
        print()                # print is here rto break the loop and print the next row

'''
Also written as

def print_square(size):
    for i in range(size):    # i represents row
        print("#" * size)

'''

main3()