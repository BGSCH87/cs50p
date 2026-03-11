def vending_machine(item_price):
    inserted_total = 0

    # 1. Collection Phase
    while inserted_total < item_price:
        print(f"Amount Due: {item_price - inserted_total}")
        try:
            coin = int(input("Insert Coin (5, 10, 25): "))
            if coin in [5, 10, 25]:
                inserted_total += coin
            else:
                print("Invalid coin.")
        except ValueError:
            print("Please enter a number.")

    # 2. Calculation Phase
    change_amount = inserted_total - item_price
    
    quarters = change_amount // 25
    remainder = change_amount % 25
    
    dimes = remainder // 10
    remainder %= 10
    
    nickels = remainder // 5
    pennies = remainder % 5

    # 3. Clean Output Phase
    change_items = []
    if quarters > 0: change_items.append(f"{quarters} Quarter(s)")
    if dimes > 0:    change_items.append(f"{dimes} Dime(s)")
    if nickels > 0:  change_items.append(f"{nickels} Nickel(s)")
    if pennies > 0:  change_items.append(f"{pennies} Penny/Pennies")

    if change_items:
        print(f"Dispensing: {', '.join(change_items)}")
    else:
        print("Exact change. Thank you!")

# --- Now you can run it for different prices easily ---
print("--- Buying a Soda ---")
vending_machine(50)

print("\n--- Buying a Snack ---")
vending_machine(75)