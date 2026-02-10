import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
api_url = "https://api.tradewatch.io/currencies/quotes?symbols=EURGBP,CHFUSD"
headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json"
}

def fetch_data(url, headers):
    print(f"Fetching financial data from FinancialData...")
    try:
        response = requests.get(url, headers)
        response.raise_for_status()  # Raise an error for bad status codes
        print("API request successful.")
        data = response.json()
        print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise

def mock_fetch_data():
    print("Mock fetching financial data...")
    data = {'items': [{'symbol': 'EURGBP', 
                       'ask': 0.87179, 
                       'bid': 0.87153, 
                       'mid': 0.87166, 
                       'timestamp': 1770755943890}, 
                       {'symbol': 'CHFUSD', 
                        'ask': 1.30302, 
                        'bid': 1.3032, 
                        'mid': 1.30311, 
                        'timestamp': 1770755944127}]}
    return data

mock_fetch_data()