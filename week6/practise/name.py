#create an empty list
names = []

#ask user for name
name = input("What's your name? ")

#write name to the names.txt
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

#read names from names.txt
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

#iterate over names while sorting
for name in sorted(names):
    print(f"hello, {name}")