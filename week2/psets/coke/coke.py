i = 50
while i > 0:
    print("Amount left: " + str(abs(i)))
    x = int(input("Enter a coin: "))
    if x in [25, 10, 5, 1]:
        i = i - x
    else:
        continue
    

print("Change: " + str(abs(i)))