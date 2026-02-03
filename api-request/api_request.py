import requests

api_url = "https://financialdata.net/api/v1/stock-prices?identifier=MSFT&key=94b3102bc654595797b65052eba1573c"

def fetch_data(url):
    print(f"Fetching financial data from FinancialData...")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        print("API request successful.")
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
    
def mock_fetch_data():
    print("Mock fetching financial data from FinancialData...")
    return [{'trading_symbol': 'MSFT', 'date': '2026-01-30', 'open': 439.17, 'high': 439.6, 'low': 426.45, 'close': 430.29, 'volume': 58566820.0}, {'trading_symbol': 'MSFT', 'date': '2026-01-29', 'open': 439.99, 'high': 442.5, 'low': 421.02, 'close': 433.5, 'volume': 128855300.0}, {'trading_symbol': 'MSFT', 'date': '2026-01-28', 'open': 483.21, 'high': 483.74, 'low': 478.0, 'close': 481.63, 'volume': 36875400.0}, {'trading_symbol': 'MSFT', 'date': '2026-01-27', 'open': 473.7, 'high': 482.87, 'low': 473.16, 'close': 480.58, 'volume': 29213920.0}]