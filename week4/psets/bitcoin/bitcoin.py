import sys
import requests

def main():
    # 1. Check for the correct number of arguments
    if len(sys.argv) != 2:
        sys.exit(1)
        
    # 2. Try to convert input to a float
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit(1)

    # 3. Fetch the data with error handling
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=09205ff9dbacf2bba592dcb9c97515ce3555430c6ce6721a301f49b250987317"
        )
        
        # Check if the request was successful (e.g., status 200)
        response.raise_for_status() 

        o = response.json()
        price = o["data"]["priceUsd"]
        user_req = float(price) * n
        print(f"${user_req:,.4f}")

    except requests.RequestException as e:
        # This catches any web-related errors (no internet, 404, etc.)
        sys.exit(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()