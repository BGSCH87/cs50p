list = {}

while True: 
    try: 
        item= input().upper().strip()
        if item not in list: 
            list[item] = 1
        else:
            list[item] += 1
    except (EOFError, KeyError) :
        print("\n--- Summary ---")
        break

for item in sorted(list):
    print(f"{list[item]} {item}")