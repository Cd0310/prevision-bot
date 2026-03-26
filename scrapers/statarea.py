from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

def get_html(url):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    return requests.get(url, headers=headers).text

def scrape_statarea():
    url = "https://statarea.com/predictions"
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")

    data = []

    for row in soup.select("tr"):
        text = row.get_text(" ", strip=True)
        if text:
            data.append({"site": "statarea", "raw": text})

    return data
