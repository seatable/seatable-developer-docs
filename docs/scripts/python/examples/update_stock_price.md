# Watch stock price by querying an API

This Python script demonstrates how to retrieve data from an external source by making a `GET` request to an external API. The [Twelve Data](https://twelvedata.com) API is indeed used to update and maintain current stock prices within a designated SeaTable table. 

!!! info "Free subscription and fake/mock APIs"
    A free subscription is available for Twelve Data if you just want to test the script (up to 800 calls per days are free). 
    
    If you're interested in querying external APIs, you can find free playground APIs for such purpose such as the very specific [cat API](https://thecatapi.com/), [JSONPlaceholder](https://jsonplaceholder.typicode.com/) or more complex mock API such as [MockFast.io](https://mockfast.io/) allowing you to define the structure of the response for more complex and heavy testing.

Here is the structure of the table named `Watch stock` you need so that this script could run (variables are present at the beginning of the script to easily adapt the names):

| Column name | Symbol | Current stock price | 
| ----------- |: ------ :|: ------ :|
| **Column type**  |  text   |   number (dollar)  |

You can create several lines to watch current stock price, for example by specifying *AAPL* or *AMZN* for the `Symbol` column.

## Process Overview

1. **Initializes configurations** for the Twelve Data API and SeaTable server.
2. **Fetches current stock prices** using the Twelve Data API based on stock symbols from a SeaTable table (from the `Symbol` column in the `Watch stock` table).
3. **Updates the SeaTable table** with the fetched current stock prices in the designated column (`Current stock price`).
4. **Displays the updated stock prices** for each symbol in the console.

This script enables the automated update of current stock prices within a SeaTable table by leveraging data from the Twelve Data API, ensuring that stock information remains up-to-date within the SeaTable environment.

## Code

```python
from seatable_api import Base, context
import requests
"""
This Python script integrates data from the Twelve Data API with SeaTable
to update and maintain current stock prices.
"""

# 1. Configuration variables for both SeaTable and Twelve Data
TWELVE_DATA_API_KEY = "dfb122bbca6a4..."  # Replace this with your actual API key from Twelve Data

SERVER_URL = context.server_url or "https://cloud.seatable.io/"
API_TOKEN = context.api_token or "..."

TABLE_WITH_STOCK_SYMBOLS = "Stock watch"
COLUMN_WITH_STOCK_SYMBOLS = "Symbol"
COLUMN_WITH_STOCK_PRICE = "Current stock price"

def get_stock_price(SYMBOL):
    # Endpoint to fetch current stock price
    url = f"https://api.twelvedata.com/price?symbol={SYMBOL}&apikey={TWELVE_DATA_API_KEY}"

    # Make the GET request to fetch the data
    response = requests.get(url)

    if response.status_code == 200:
        output = response.json()
        return output['price']
    else:
        return false

# Get symbols from SeaTable base and update the current stock prices
def update_stock_price():
    for row in base.list_rows(TABLE_WITH_STOCK_SYMBOLS):
        # 2. Fetches the current stock price from Twelve Data API
        current_price = get_stock_price(row['Symbol'])
        # 3. Update the stock price in the table
        base.update_row(TABLE_WITH_STOCK_SYMBOLS, row.get('_id'), {COLUMN_WITH_STOCK_PRICE: current_price})
        # 4. Display the fetched value in the console
        print(f"The current price of {row['Symbol']} is: {current_price}")

if __name__ == '__main__':
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()
    update_stock_price()
    print("Update complete.")
```
