sum = input("Sum: ").strip()


x, y, z = sum.split(" ")

n1 = float(x)
n2 = float(z)

if y == "+":
    result = n1 + n2
elif y == "-":
    result = n1 - n2
elif y == "*":
    result = n1 * n2
elif y == "/":
    # The problem guarantees n2 will not be 0 for division
    result = n1 / n2

print(f"{result:.1f}")

