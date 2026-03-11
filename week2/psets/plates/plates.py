#requiremens:
## 2. All plates must start with at least two letters.”
## 1. Maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
## 5. Numbers cannot be used in the middle of a plate, only at the end of the plate.
## 4. First number cannot be 0
## 3. No periods, spaces, or punctuation marks are allowed.

#TODO: check if the plate is valid


def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(p):
    # 1. Check length (2 to 6 characters)
    if len(p) < 2 or len(p) > 6:
        return False

    # 2. Check if first two characters are letters
    if not p[0:2].isalpha():
        return False

    # 3. Check for invalid characters (symbols/spaces)
    if not p.isalnum():
        return False

    # 4. Check number placement and the "no leading zero" rule
    for i in range(len(p)):
        if p[i].isdigit():
            # If the first number found is '0', it's invalid
            if p[i] == '0':
                return False
            
            # 5. Check if the rest of the characters are all numbers
            if not p[i:].isdigit():
                return False

            # we can stop checking
            break

    # If all checks pass
    return True
    







main()