name = input("What is your name? ")

name = name.strip() #remove whitespaces from string. Means remove spaces.

name = name.capitalize() #This capitalize the first letter of the input words.

name = name.title() #This capitalize the first letter of all the input words.

first, last = name.split(" ")#This splits the input words into the designated variables

'''
we can also write as ' name = name.strip().title() ' 
or ' name = input("What is your name? ").strip().title() '

''' 
print (f"Hello {name}")  # type: ignore

print (f"Hello {first}")  # type: ignore