import sys
from pyfiglet import Figlet
import random



def main():

    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        s = input("Input: ")
        figlet.setFont(font=random.choice(fonts))
        print(figlet.renderText(s))
    elif len(sys.argv) == 2 or len(sys.argv) >3:
        print("Invalid usage")
        sys.exit(1)
    elif len(sys.argv) == 3 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print("Invalid usage")
        sys.exit(1)
    elif len(sys.argv) == 3 and sys.argv[2] not in fonts:
        print("Invalid usage")
        sys.exit(1)
    else:  
        s = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
    

if __name__ == "__main__":
    main()
        
