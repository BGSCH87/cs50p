def main():

    user_input = input("Greeting: ")
    user_input = user_input.strip().lower()

    output = value(user_input)
    print(output)

def value(greeting):
    #if greeting starts with hello -> $0
    if (greeting.startswith("hello")):
        greeting =  int(0)
        return greeting
        #if greeting starts with 'h', but not hello -> $20
    elif (greeting.startswith("h")) and (greeting != 'hello'):
        greeting = int(20)
        return greeting
        #otherwise $100
    else:
        greeting = int(100)
        return greeting


if __name__ == "__main__":
    main()