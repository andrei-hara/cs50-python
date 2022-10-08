import json
import requests
import sys

# taking the command line argument
if len(sys.argv) == 2:
    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

# getting the api response from server
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# taking the value of a bitcoin in USD
o = response.json()
currency = o["bpi"]
value = currency["USD"]
course = (value["rate"])

thousands, hundreds = course.split(",")

# storing the value in a float variable
bitcoin_value = (float(thousands) * 1000 + float(hundreds)) * bitcoin
print(f"${bitcoin_value:,.4f}")
