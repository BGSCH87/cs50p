for i in [0, 1, 2, 3]:
    print("meow" * i)

print()

for i in range(10):
    print("meow")
print()

#start from 5 and go UP to 10
for i in range(5, 10):
    print(i)
print()

#start from 0 and go UP to 10 with a step of 2
for i in range(0, 10, 2):
    print(i)



print()

names = ["Ron", "Basje", "Piet", "Jan"]

#print out the first name in the list 
print(names[0])

print()
#print all names in the list
for name in names:
    print(name)

print()

#print all names in the list
for i in range(len(names)):
    print(names[i])

print()
#print all the names with there index remove the zero index
for studient in range(len(names)):
    print(i + 1, names[i])

print()
#print all names in the list and their index
for i, name in enumerate(names):
    print(i, name)

print()
#print out all names in the list and their index starting from 1
for i, name in enumerate(names, 1):
    print(i, name)

print()
#print out all names in the list backwards
for i in range(len(names) - 1, -1, -1):
    print(names[i])