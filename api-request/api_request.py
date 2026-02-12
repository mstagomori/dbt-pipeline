import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
api_url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=Rio de Janeiro"

def fetch_data():
    print(f"Fetching weather data from weatherstack...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        print("API request successful.")
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise