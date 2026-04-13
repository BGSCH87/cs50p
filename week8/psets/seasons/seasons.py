from datetime import date, datetime
import sys
import inflect

p = inflect.engine()

def main():
    input_date = input("Date: ")
    
    try:
        born = datetime.strptime(input_date, "%Y-%m-%d").date()
        if born > date.today():
            sys.exit(1)
    except ValueError:
        sys.exit(1)

    # Use the helper functions
    minutes = calculate_age(born, date.today())
    words = inflect_minutes(minutes)
    
    # Capitalize the first letter and print
    print(f"{words.capitalize()} minutes")

def calculate_age(bday, today):
    diff = today - bday
    return diff.days * 24 * 60

def inflect_minutes(age):
    # andword="" removes the "and" (e.g., "five hundred twenty-five")
    return p.number_to_words(age, andword="")

if __name__ == "__main__":
    main()