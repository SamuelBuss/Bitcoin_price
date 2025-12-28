import requests
import json

SUPPORTED_CURRENCIES = [
    "aed", "ars", "aud", "bdt", "bhd", "bmd", "brl", "cad", "chf", "clp",
    "cny", "czk", "dkk", "eur", "gbp", "gel", "hkd", "huf", "idr", "ils",
    "inr", "jpy", "krw", "kwd", "lkr", "mmk", "mxn", "myr", "ngn", "nok",
    "nzd", "php", "pkr", "pln", "rub", "sar", "sek", "sgd", "thb", "try",
    "twd", "uah", "usd", "vef", "vnd", "zar",
]

# Keep asking until we get a supported currency code
while True:
    currency = input("What currency would you like to see the Bitcoin price in?: ").strip().lower()
    if currency in SUPPORTED_CURRENCIES:
        break
    print("Unsupported currency. Please choose one from README.md")

# Build URL for the chosen currency code
api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=" + currency

try:
    # Send the GET request to the API
    response = requests.get(api_url)

    # Raise an exception if the request failed (e.g., status 404, 500)
    response.raise_for_status()

    # Parse the JSON response into a Python dictionary
    data = response.json()

    # Extract the specific price data
    bitcoin_price = data.get('bitcoin', {}).get(currency)

    if bitcoin_price is not None:
        print(f"The current price of Bitcoin is: {bitcoin_price:,.2f} {currency.upper()}")
    else:
        print("Could not find the price in the response.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the API request: {e}")
except json.JSONDecodeError:
    print("Failed to decode JSON response.")