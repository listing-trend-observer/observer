import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# 1. Go to the website
url = "https://www.dvcresalemarket.com/listings/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 2. Find all the rows in the table
listings = soup.find_all('tr', class_='listings-table__listing')

# 3. Open our "Notebook" to add new data
with open('data/listings_history.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    today = datetime.now().strftime('%Y-%m-%d')

    for item in listings:
        # Using the "Spy Mission" labels you found!
        resort = item.find('a', class_='listings-table__listing-resort').text.strip()
        points = item.find('td', {'data-column': 'points'}).text.strip()
        price = item.find('td', {'data-column': 'price-per-point'}).text.strip()
        
        writer.writerow([today, resort, points, price])

print("Robot mission complete: Data saved!")
