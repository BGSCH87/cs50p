user_input = input("Greeting: ")

user_input = user_input.strip().lower()

#if greeting starts with hello -> $0
if (user_input.startswith("hello")):
    print("$0")
    #if greeting starts with 'h', but not hello -> $20
elif (user_input.startswith("h")) and (user_input != 'hello'):
    print("$20")
    #otherwise $100
else:
    print("$100")




