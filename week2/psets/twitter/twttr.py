input = input("Write me something: ")

for cc in input:
    if cc in ["a", "e", "i", "o", "u"] or cc in ["A", "E", "I", "O", "U"]:
        continue
    print(cc, end="")