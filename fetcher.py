import requests

# Base URL for the CoinGecko API
BASE_URL = "https://api.coingecko.com/api/v3"

def fetch_crypto_prices():
    """
    Fetches the top 10 cryptocurrencies by market cap.
    """
    # Endpoint for fetching cryptocurrency market data
    endpoint = f"{BASE_URL}/coins/markets"
    
    # Parameters for the API request
    params = {
        "vs_currency": "usd",  # Currency to display prices in
        "order": "market_cap_desc",  # Order by market cap descending
        "per_page": 10,  # Number of results per page
        "page": 1,  # Page number
        "sparkline": False,  # Exclude sparkline data
    }
    
    try:
        # Make the API request
        response = requests.get(endpoint, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract relevant data for each cryptocurrency
            return [
                {
                    "name": coin["name"],  # Name of the cryptocurrency
                    "symbol": coin["symbol"].upper(),  # Symbol of the cryptocurrency
                    "price": coin["current_price"],  # Current price
                    "change_24h": coin["price_change_percentage_24h"],  # 24-hour price change percentage
                    "market_cap": coin["market_cap"],  # Market capitalization
                }
                for coin in data
            ]
        else:
            # Print an error message if the request failed
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        # Print an error message if an exception occurred
        print(f"Error occurred: {e}")
        return None


def search_crypto(coin_name):
    
    # Endpoint for searching cryptocurrency market data
    endpoint = f"{BASE_URL}/coins/markets"
    
    # Parameters for the API request
    params = {
        "vs_currency": "usd",  # Convert prices to USD
        "ids": coin_name.lower(),  # CoinGecko API requires lowercase for coin IDs
    }

    try:
        # Make the API request
        response = requests.get(endpoint, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            if data:
                # Extract relevant details
                coin = data[0]
                return {
                    "name": coin["name"],  # Name of the cryptocurrency
                    "symbol": coin["symbol"].upper(),  # Symbol of the cryptocurrency
                    "price": coin["current_price"],  # Current price
                    "change_24h": coin["price_change_percentage_24h"],  # 24-hour price change percentage
                    "market_cap": coin["market_cap"],  # Market capitalization
                }
            else:
                # Print an error message if no data was found
                print(f"No data found for {coin_name}")
                return None
        else:
            # Print an error message if the request failed
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        # Print an error message if an exception occurred
        print(f"Error occurred: {e}")
        return None
