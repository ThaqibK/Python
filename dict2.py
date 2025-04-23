students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}    # None is a keyword represents absent of value 
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")