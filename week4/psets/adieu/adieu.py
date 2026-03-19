import inflect


# prompt the user for a name
def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            #if all well get the name and append it to the list called nnaames. 
            name = input("Name: ")
            #if name is empty reprompt user for name
            if not name:
                continue
            #append name to names list
            names.append(name)
        #When end of file or keyboard interupt, print new line and interupt program
        except (EOFError, KeyboardInterrupt):
            print()
            break
    #join function from inflect to join the names and prepend the adieu call
    if names:
        namelist = p.join(names)
        print("Adieu, adieu, to", namelist)


main()
