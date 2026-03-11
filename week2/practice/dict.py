dict = {
    "Bas": "Nieuwaal",
    "Jan": "Veldhoven",
    "Piet": "Maarssen",
    "Ron": "Utrecht"
}

for name, city in dict.items():
    print(f"{name} is from {city}")

dict.update({"Basje" : "Utrecht"})

print()
for name, city in dict.items():
    print(f"{name} is from {city}")


dict = [
    {"name": "Bas", "city": "Nieuwaal", "age": 20},
    {"name": "Jan", "city": "Veldhoven", "age": 21},
    {"name": "Piet", "city": "Maarssen", "age": 22},
    {"name": "Ron", "city": "Utrecht", "age": None}
]

for person in dict:
    print(f"{person['name']} is from {person['city']} and is {person['age']} years old")
