import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# 1. Fetch the website
url = "https://www.dvcresalemarket.com/listings/"
headers = {'User-Agent': 'Mozilla/5.0'} # Helps the robot look like a real person
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 2. Find all listing rows
listings = soup.find_all('tr', class_='listings-table__listing')

# 3. Open the notebook
file_path = 'data/listings_history.csv'
today = datetime.now().strftime('%Y-%m-%d')

with open(file_path, 'a', newline='') as f:
    writer = csv.writer(f)
    
    for item in listings:
        try:
            # We use a more flexible way to find the data you pointed out
            resort = item.find('td', {'data-column': 'resort'}).text.strip()
            points = item.find('td', {'data-column': 'points'}).text.strip()
            price = item.find('td', {'data-column': 'price-per-point'}).text.strip()
            
            # Calculate total price (Price * Points)
            clean_price = float(price.replace('$', '').replace(',', ''))
            clean_points = int(points.replace(',', ''))
            total = f"${clean_price * clean_points:,.2f}"

            writer.writerow([today, resort, points, price, total])
        except Exception as e:
            # If one row is weird, skip it and keep going
            continue

print(f"Robot successfully recorded {len(listings)} listings!")
