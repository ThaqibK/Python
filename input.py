name = input("What is your name? \n")

#type-1
print("Hello "+ name) 

#type-2 ',' for multiple concantations
print("Hello", name,". Nice to meet you", name) 

#type-3 
print ("hello", end=" ") #here the end argument decides what to be given at the end of the line. We can give space or \n - new line inside the quotes.
print (name)

#type-4
print ("hello", name, sep=" ") #here the sep argument decides what to be given between the hello and name. We can give space or \n - new line inside the quotes.

#type-5
print (f"Hello {name}") #'f' represents formating and the word should be inside the curly braces.