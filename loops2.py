def main():
    num = get_num()
    meow(num)

def meow(n):
    for _ in range (n):
        print ("meow!")

def get_num():
    while True:
        n = int(input("Enter the value: "))
        if n>0:
            break
    return n

'''
Can also written as 

def get_num(i):
    while True:
        n = int(input("Enter the value: "))
        if n>0:
            return n
'''
main()