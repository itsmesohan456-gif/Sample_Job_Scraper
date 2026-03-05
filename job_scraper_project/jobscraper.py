import requests
from bs4 import BeautifulSoup
import pandas as pd

def run_scraper():
    target_url = "https://quotes.toscrape.com/"

    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/ 537.36"

    }
    print(f"Connecting to {target_url}...")

    response = requests.get(target_url, headers=headers)

    if response.status_code == 200:
        print("Success! Page retrieved.")
    else:
        print("Failed to connect. Error code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')

    extracted_data = []
    

