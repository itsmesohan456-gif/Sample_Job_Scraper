import requests
from bs4 import BeautifulSoup
import pandas as pd

def run_scraper():
    target_url = "https://quotes.toscrape.com/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/ 537.36"

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
    
    quotes = soup.find_all('div', class_='quote')

    for q in quotes:
        text = q.find("span", class_='text').text
        author = q.find("small", class_='author').text
        
        extracted_data.append({
            'Quote Content': text.replace('"','').replace('""',''),
            'Author Name': author                           
        })
    df = pd.DataFrame(extracted_data)

    df.to_csv('my_scraped_data.csv', index=False)

    print("--- SCRAPING COMPLETED ---")
    print(f"Found {len(extracted_data)} items")
    print(f"Check your folder for 'my_scraped_data.csv'!")

if __name__ == "__main__":
     run_scraper()

