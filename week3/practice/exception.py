def main():

    while True:
        try:
            y = int(input("What's y? "))    
        except ValueError:
            print("That's not a number.")
        else: 
            break 
    print(f"y is {y}")


## make get_int function 

    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("That's not a number.")
            #je kunt ook pass gebruiken

main()