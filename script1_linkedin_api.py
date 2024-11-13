import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


ACCESS_TOKEN = 'your_token'
# Base API URL for future modifications (change this based on your chosen API endpoint)
BASE_API_URL = 'https://api.linkedin.com/v2/people/'

def get_linkedin_data(user_id=None):
  """
  Fetches LinkedIn data for a specific user (if user_id provided) or the logged-in user (using "me" endpoint).
  """
  headers = {
      'Authorization': f'Bearer {ACCESS_TOKEN}'
  }

  # Construct the API URL based on the user_id
  api_url = BASE_API_URL + 'me' if not user_id else BASE_API_URL + f'(id:{user_id})'

  response = requests.get(api_url, headers=headers)

  if response.status_code == 200:
    logging.info("API call successful!")
    return response.json()
  else:
    logging.error(f"API call failed with status code: {response.status_code}")
    return None

def save_to_csv(data, filename='users_data.csv'):
  """
  Saves data to a CSV file (skips if data is None).
  """
  if data:
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)
    logging.info(f"Data saved to {filename}")
  else:
    logging.error("No data to save.")

def main():
  """
  Prompts for user input (optional for future People Search implementation) and calls data retrieval functions.
  """
  
  
  user_id = None  # Replace with user ID if available

  data = get_linkedin_data(user_id)  # Use user_id if available
  if data:
    save_to_csv(data)

if __name__ == '__main__':
  main()