import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit(ValueError)

def convert(s):
    # This regex captures: Hour, optional Minutes, and AM/PM for both times
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    
    if matches := re.search(pattern, s):
        # Unpack the 6 groups captured by the regex
        h1, m1, p1, h2, m2, p2 = matches.groups()
        

        time_start = format_24(h1, m1, p1)
        time_end = format_24(h2, m2, p2)
        
        return f"{time_start} to {time_end}"
    else:
        raise ValueError

def format_24(hour, minute, period):
    h = int(hour)
    # If minute is None (like in "9 AM"), set it to 0
    m = int(minute) if minute else 0
    
    # Validation: Hours must be 1-12, Minutes must be 0-59
    if h > 12 or m > 59:
        raise ValueError

    # The 24-hour conversion "Magic":
    if period == "PM" and h != 12:
        h += 12
    elif period == "AM" and h == 12:
        h = 0
        
    # Return formatted as HH:MM (the :02 ensures a leading zero like 09:00)
    return f"{h:02}:{m:02}"

if __name__ == "__main__":
    main()