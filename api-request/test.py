import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
api_url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=Rio de Janeiro"

response = requests.get(api_url)
response.raise_for_status()  # Raise an error for bad status codes
print("API request successful.")
data = response.json()

print(data)