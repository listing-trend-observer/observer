import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# 1. Fetch the website
url = "https://www.dvcresalemarket.com/listings/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

listings = soup.find_all('tr', class_='listings-table__listing')

file_path = 'data/listings_history.csv'
today = datetime.now().strftime('%Y-%m-%d')
saved_count = 0

with open(file_path, 'a', newline='') as f:
    writer = csv.writer(f)
    
    for item in listings:
        try:
            # --- NEW: Grab the Unique Link/ID ---
            link_element = item.find('a', class_='listings-table__listing-resort')
            listing_url = link_element['href'] if link_element else "N/A"
            # Extract just the ID from the end of the URL (e.g., 'vcl-24601')
            listing_id = listing_url.split('/')[-2] if '/' in listing_url else "N/A"

            # Grab the rest of the data
            resort = link_element.get_text(strip=True) if link_element else "Unknown"
            points = item.find('td', {'data-column': 'points'}).get_text(strip=True)
            price = item.find('td', {'data-column': 'price-per-point'}).get_text(strip=True)
            
            # Save it! (Adding listing_id as a new column)
            writer.writerow([today, listing_id, resort, points, price])
            saved_count += 1
        except Exception:
            continue

print(f"Recorded {saved_count} listings with unique IDs!")

# --- NEW: DEAL ALERT LOGIC ---
deals = []
for item in listings:
    try:
        resort = item.find('a', class_='listings-table__listing-resort').get_text(strip=True)
        price_text = item.find('td', {'data-column': 'price-per-point'}).get_text(strip=True)
        price = float(price_text.replace('$', ''))
        
        # Customize your alert criteria here!
        if "AnimalKingdom" in resort and price < 110:
            deals.append(f"AKL DEAL: ${price}/pt (ID: {resort})")
    except:
        continue

# If deals are found, write them to a temporary file for the next step
if deals:
    with open("alerts.txt", "w") as f:
        f.write("\n".join(deals))

