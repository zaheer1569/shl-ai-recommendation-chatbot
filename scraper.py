import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://www.shl.com"

catalog_url = "https://www.shl.com/solutions/products/product-catalog/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(catalog_url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

catalog = []
visited = set()

for link in links:

    href = link.get("href")

    if href and "/products/" in href:

        full_url = href if href.startswith("http") else BASE_URL + href

        if full_url in visited:
            continue

        visited.add(full_url)

        print("Scraping:", full_url)

        try:
            product_page = requests.get(full_url, headers=headers)

            product_soup = BeautifulSoup(product_page.text, "html.parser")

            title = product_soup.find("h1")

            title_text = title.get_text(strip=True) if title else "Unknown"

            paragraphs = product_soup.find_all("p")

            clean_paragraphs = []

            for p in paragraphs:

                text = p.get_text(strip=True)

                if len(text) < 40:
                     continue

                if "upgrade your browser" in text.lower():
                    continue

                if "javascript" in text.lower():
                    continue

                clean_paragraphs.append(text)

            description = " ".join(clean_paragraphs[:5])
            
            catalog.append({
                "name": title_text,
                "url": full_url,
                "description": description
            })

            time.sleep(1)

        except Exception as e:
            print("Error:", e)

with open("catalog.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=4, ensure_ascii=False)

print(f"Saved {len(catalog)} products!")