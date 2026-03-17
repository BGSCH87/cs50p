def main():
    #check for these date formats: 
    # 9/8/1636
    # September 8, 1636

    while True:
        try:
            date = input("Date: ")
            if date.count("/") == 2:
                date_s = date.split("/")
                get_date_slash(date_s)
                break
            elif date.count(" ") == 2:
                date_w = date.split(" ")
                get_date_word(date_w)
                break
        except (ValueError, IndexError):
            # We catch the error but do nothing,
            # causing the loop to start over
            pass


def get_date_slash(date_s):
    month = int(date_s[0])
    day = int(date_s[1])
    year = int(date_s[2])

    if not (1 <= month <= 12 and 1 <= day <= 31):
        raise ValueError

    print(f"{year}-{month:02}-{day:02}")


def get_date_word(date_w):
    months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
    if date_w[0] not in months:
        raise ValueError
    #check if there is a comma
    if not date_w[1].endswith(","):
        raise ValueError
    #start from 1 and select the name of the month from the list
    month = months.index(date_w[0]) + 1
    #remove the comma after day
    day = int(date_w[1].replace(",", ""))
    year = int(date_w[2])

    if not (1 <= day <= 31):
        raise ValueError

    date = print(f"{year}-{month:02}-{day:02}")
    return date


if __name__ == "__main__":
    main()
