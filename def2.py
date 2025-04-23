def main(): #main is a function that contains the main code.
    name = input("What is your name? ")
    hello()


def hello(to="World"):  #assigning 'to' to 'world' as default. If the hello() is called instead of hello(name) the o/p will be Hello World
    print("Hello", to)

main() #it needs tio be called at the end or the code doesn't run. It calls the main function code then that code calls the hello function code.