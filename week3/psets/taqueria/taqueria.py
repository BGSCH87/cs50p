menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0.0
while True:
    try:
        item = input("Item: ").title() # hier gaan we de input halen en de eerste letter in hoofdletters zetten 
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
    except (EOFError, KeyboardInterrupt):
        #wanneer ctrl d stopt de loop
        print("\n")
        break