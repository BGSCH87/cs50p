from validator_collection import validators, checkers, errors

def main():
    print(validate(input("IPv4 Address: ")))

def validate(s):
    try:
        email = validators.email(s)
        return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"
    

if __name__ == "__main__":
    main()