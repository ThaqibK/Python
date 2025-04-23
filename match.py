name = input("Enter the name: ")

match name:   # This is similar to if confition
    case "Harry" | "Hermoine" | "Ron":      
        print ("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:     # here _ represents any other case except th previous mentioned
        print ("Who?")

'''
alos written as (Shortening)

match name:   # This is similar to if confition
    case "Harry":      
        print ("Gryffindor")
    case "Hermoine":
        print ("Gryffindor")
    case "Ron":
        print ("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:     # here _ represents any other case except th previous mentioned
        print ("Who?")

'''