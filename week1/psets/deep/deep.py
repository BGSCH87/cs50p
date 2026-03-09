x = input("What is  the answer to the Great Question of Life, the Universe and Everything? ")
y = x.strip()

if y == "42":
    print("Yes")
elif y.title() == "Forty-Two" or y.title() == "Forty Two":
    print("Yes")
else:
    print("No")
