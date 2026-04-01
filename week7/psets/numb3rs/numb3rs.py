import re
import sys


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


# implement a function called validate that expects an IPv4 address as input as a str and then returns True or False
def validate(ip):

    if re.search(r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
