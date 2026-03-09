def main():

    emo = input("please enter a nice hello message with a happy or sad smiley: ")
    convert(emo)


def convert(str):
    new_text = str.replace(":)", "🙂").replace(":(", "🙁")
    print(new_text)


main()
