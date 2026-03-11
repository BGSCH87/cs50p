cc = input("CamelCase: ")

print("snake_case: ", end="")

for c in cc:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")
print()