import emoji

def main():

    name = input("Enter an emoji name: ")
    print (emoji.emojize(f"{name}", language="en"))



if __name__ == "__main__":
    main()