import sys
import requests


def main():
    # Check if the user provided the argument
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        # Try to convert the first argument (index 1) to a float
        n = float(sys.argv[1])
    except ValueError:
        sys.exit(1)
    try:
        response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=09205ff9dbacf2bba592dcb9c97515ce3555430c6ce6721a301f49b250987317"
    )
        
    # --- PRO TIP #1 START ---
    # This checks if the request was successful (status code 200).
    # If it's a 404 (Not Found) or 500 (Server Error), it raises an exception.
    response.raise_for_status() 
    # --- PRO TIP #1 END ---

    o = response.json()
    price = o["data"]["priceUsd"]
    user_req = float(price) * n
    print(f"${user_req:,.4f}")

        # --- PRO TIP #2 START ---
    except requests.RequestException as e:
    # This catches any web-related errors (like no internet or a bad URL)
    sys.exit(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()