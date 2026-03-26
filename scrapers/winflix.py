import requests
from bs4 import BeautifulSoup

def scrape_winflix():
    url = "https://winflix.co/predictions"

    try:
        html = requests.get(url, timeout=10).text
    except:
        return []

    soup = BeautifulSoup(html, "lxml")

    matches = []

    for div in soup.find_all("div"):
        text = div.get_text(" ", strip=True)

        if "vs" in text:
            matches.append({
                "site": "winflix",
                "raw": text
            })

    return matches
