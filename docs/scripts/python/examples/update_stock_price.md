# Stock Price Update with Twelve Data API

This Python script integrates data from the Twelve Data API with SeaTable to update and maintain current stock prices within a designated SeaTable table.

## Functionality

- **Configuration Setup**: Defines configurations for the Twelve Data API and SeaTable server, specifying API keys and table/column details within SeaTable.
- **Stock Price Retrieval**:

      - Utilizes the Twelve Data API to retrieve the current stock prices based on stock symbols.
      - Makes HTTP GET requests to the Twelve Data API to fetch stock prices using the provided API key.

- **SeaTable Update**:

      - Retrieves stock symbols from a designated SeaTable table (Stock Watch).
      - Updates the SeaTable table with the current stock prices fetched from the Twelve Data API, populating the designated column (Current stock price) in SeaTable.
      - Displays the updated stock prices for each symbol in the console.

## Process Overview

1. Initializes configurations for the Twelve Data API and SeaTable server.
1. Fetches current stock prices using the Twelve Data API based on stock symbols.
1. Retrieves stock symbols from the SeaTable table (Stock Watch).
1. Updates the SeaTable table with the fetched current stock prices in the designated column (Current stock price).
1. Displays the updated stock prices for each symbol in the console.

This script enables the automated update of current stock prices within a SeaTable table by leveraging data from the Twelve Data API, ensuring that stock information remains up-to-date within the SeaTable environment.

## SeaTable Base used in this example

| Symbol | Current stock price |
| ------ | ------------------- |
| AAPL   | $198.03             |
| AMZN   | $147.40             |

## Code

```python
from seatable_api import Base, context
import requests

TWELVE_DATA_API_KEY = "dfb122bbca6a4..."  # Replace this with your actual API key from Twelve Data (up to 800 calls per days are free)

SERVER_URL = context.server_url or "https://cloud.seatable.io/"
API_TOKEN = context.api_token or "..."

TABLE_WITH_STOCK_SYMBOLS = "Stock Watch"
COLUMN_WITH_STOCK_SYMBOLS = "Symbol"
COLUMN_WITH_STOCK_PRICE = "Current stock price"

###
# Do not change anything below this line
###

# Endpoint to fetch current stock price
def get_stock_price(SYMBOL):
    url = f"https://api.twelvedata.com/price?symbol={SYMBOL}&apikey={TWELVE_DATA_API_KEY}"

    # Making the GET request to fetch the data
    response = requests.get(url)

    if response.status_code == 200:
        output = response.json()
        return output['price']
    else:
        return false

# get symbols from SeaTable base and update the current stock price
def update_stock_price():
    for row in base.list_rows(TABLE_WITH_STOCK_SYMBOLS):
        current_price = get_stock_price(row['Symbol'])
        base.update_row(TABLE_WITH_STOCK_SYMBOLS, row.get('_id'), {COLUMN_WITH_STOCK_PRICE: current_price})
        print(f"The current price of {row['Symbol']} is: {current_price}")

if __name__ == '__main__':
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()
    update_stock_price()
    print("Update complete.")
```
