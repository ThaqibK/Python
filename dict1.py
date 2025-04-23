students = {
    "Hermoine": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin"
}

print (students["Hermoine"])      # prints the value of the key.

for student in students:
    print(student)                # In dictionary function for loop only gives keys. Not values. to otain values....

for student in students:
    print(student, students[student], sep=", ")  # This displays both key and value with seperator function ',' 