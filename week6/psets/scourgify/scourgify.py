import sys
import csv

def main():
    # 1. Check for exactly 3 arguments (script, input, output)
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    # 2. Ensure both files are .csv
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        # 3. Open 'before' for reading and 'after' for writing
        with open(sys.argv[1], "r") as infile, open(sys.argv[2], "w", newline="") as outfile:
            reader = csv.DictReader(infile)
            
            # Define new headers
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            # Write the header row first
            writer.writeheader()
            
            # 4. Loop through and "clean" each row
            for row in reader:
                # Split "Last, First" into two variables
                last, first = row["name"].split(", ")
                
                # Write to the new file
                writer.writerow({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()