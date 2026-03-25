students = []

with open("students.csv", "r") as file: 
    for line in file:
        name, place = line.rstrip().split(",")
        student = {"name": name, "place": place} 
        students.append(student) #list of dictionairies

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['place']}")
