def main():
    x = int(input("Enter the value of x : "))
    print("x squared is", square(x))


def square(n):
    return n * n # can also be written as n**2 or pow(n,2)
# This return function just returns the value.

main()