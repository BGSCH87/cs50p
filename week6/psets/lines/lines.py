import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("")
    else: 
        try:
            count = 0 
            with open(sys.argv[1]) as file:
                for line in file:
                    line = line.lstrip()
                    if line.startswith("#") == False and line.strip() != "":
                        count += 1
            print(count)
        except FileNotFoundError:
            sys.exit("") 


if __name__ == "__main__":
    main()


