import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# 1. Fetch the website
url = "https://www.dvcresalemarket.com/listings/"
headers = {'User-Agent': 'Mozilla/5.0'} 
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 2. Find all listing rows
listings = soup.find_all('tr', class_='listings-table__listing')
print(f"Found {len(listings)} listings on the page.")

# 3. Open the notebook
file_path = 'data/listings_history.csv'
today = datetime.now().strftime('%Y-%m-%d')

count = 0
with open(file_path, 'a', newline='') as f:
    writer = csv.writer(f)
    
    for item in listings:
        try:
            # Flexible labels to ensure we grab the data
            resort = item.find('td', {'data-column': 'resort'}).get_text(strip=True)
            points = item.find('td', {'data-column': 'points'}).get_text(strip=True)
            price = item.find('td', {'data-column': 'price-per-point'}).get_text(strip=True)
            
            # Save to CSV
            writer.writerow([today, resort, points, price, ""])
            count += 1
        except Exception:
            continue

print(f"Successfully wrote {count} rows to {file_path}")
