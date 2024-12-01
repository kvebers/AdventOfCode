import requests
import os
from dotenv import load_dotenv

load_dotenv()
def getData():
    url = 'https://adventofcode.com/2024/day/1/input'
    cookies = {'session': os.getenv('COOKIES')}
    if not cookies['session']:
        print("Error: Session token is missing in the .env file.")
        return
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        data = response.text.strip()
        return data
    else:
        print(f"Error: Unable to fetch data. HTTP Status Code: {response.status_code}")
        return None

