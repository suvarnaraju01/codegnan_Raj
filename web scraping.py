import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

# Step 1: Web Scraping
url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'    # Fix encoding issue
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

names = []
prices = []

for book in books:
    name = book.h3.a["title"]

    # Get raw price text
    price_text = book.find("p", class_="price_color").text

    # Extract numeric value using regex (fix for Â£ issue)
    price = float(re.findall(r'\d+\.\d+', price_text)[0])

    names.append(name)
    prices.append(price)

# Step 2: Store Data in Table
df = pd.DataFrame({
    "Book Name": names,
    "Price": prices
})

print("\n Table Data:\n")
print(df.head())

# Save to CSV
df.to_csv("books_data.csv", index=False)
print("\n CSV file 'books_data.csv' created successfully")

# Step 3: Data Visualization
plt.figure()
plt.bar(names[:10], prices[:10])    # Top 10 books
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices (Top 10)")
plt.tight_layout()
plt.show()
