def main():
    while True:
        fuelq = input("Fraction: ")
        try:
            #hieronder gaan we de functie in en berekenen het percentage
            percentage = convert(fuelq)
            print(gauge(percentage))
            break # als het goed gaat, breaken we de loop
        except (ValueError, ZeroDivisionError):
            # de ValueError en ZeroDivisionError gaan we hier opvangen en de tekst komt uit de functie
            # als het niet deelbaar is of er iets raars is, gaan we hier door
            # pass betekent "do nothing"
            pass

    # hier komen we na de loop en percentage is berekend en is niet <=0 of >1
    


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    ##hier raisen we de error en sturen deze naar de main
    if x > y:
        raise ValueError ("Something went wrong with your fraction")
    elif x < 0:
        raise ValueError ("You messed up")

    return round((x / y) * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()