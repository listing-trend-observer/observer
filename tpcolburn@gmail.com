import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# 1. Fetch the website with a "Real Person" header
url = "https://www.dvcresalemarket.com/listings/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 2. Find the listing rows
listings = soup.find_all('tr', class_='listings-table__listing')
print(f"Found {len(listings)} listings on the page.")

file_path = 'data/listings_history.csv'
today = datetime.now().strftime('%Y-%m-%d')
saved_count = 0

with open(file_path, 'a', newline='') as f:
    writer = csv.writer(f)
    
    for item in listings:
        try:
            # Deep Search for the specific classes you found
            resort_element = item.find(class_='listings-table__listing-resort')
            resort = resort_element.get_text(strip=True) if resort_element else "Unknown"

            # Look for the specific data-column attributes
            points = item.find('td', {'data-column': 'points'}).get_text(strip=True)
            price = item.find('td', {'data-column': 'price-per-point'}).get_text(strip=True)
            
            # Clean the data for the CSV
            writer.writerow([today, resort, points, price, ""])
            saved_count += 1
        except Exception as e:
            continue

print(f"Successfully recorded {saved_count} rows!")
