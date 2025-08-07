import requests
from bs4 import BeautifulSoup

# 1. Fetch the HTML content of the news website
url = "https://www.bbc.com/news"  # Change this if you prefer another site
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch the page: {response.status_code}")
    exit()

# 2. Parse the HTML and extract the headlines
soup = BeautifulSoup(response.text, "html.parser")
headlines = []

# Adjust this tag selector according to the news site’s HTML structure
for h2 in soup.find_all("h2"):
    headline = h2.get_text(strip=True)
    if headline:
        headlines.append(headline)

# 3. Save headlines to a .txt file
with open("headlines.txt", "w", encoding="utf-8") as f:
    for headline in headlines:
        f.write(headline + "\n")

print("Scraped and saved headlines successfully!")
