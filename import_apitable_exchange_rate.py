# External API - using requests
import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace with your actual API endpoint
api_endpoint = os.getenv('EXCHANGE_RATE_API_ENDPOINT')
auth_token = os.getenv('EXCHANGE_RATE_API_TOKEN')

# Headers for authentication
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Content-Type": "application/json"
}

try:
    # Sending GET request to the API
    response = requests.get(api_endpoint, headers=headers)
    
    # Raise an exception if the request was unsuccessful
    response.raise_for_status()
    
    # Load the response data into JSON
    exchange_rate_data = response.json()
    
    # Save the JSON response to a file
    with open('exchange_rate_data.json', 'w') as file:
        json.dump(exchange_rate_data, file, indent=4)
    
    print("Data successfully extracted and saved to 'exchange_rate_data.json'")
    
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")
