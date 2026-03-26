import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_html(url):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    return requests.get(url, headers=headers).text


def scrape_predictz():
    url = "https://www.predictz.com/predictions/"
    html = get_html(url)

    soup = BeautifulSoup(html, "lxml")

    matches = []

    rows = soup.select("tr")

    for row in rows:
        text = row.get_text(" ", strip=True)

        # structure typique :
        # TeamA vs TeamB + odds + prediction
        if "vs" in text or "-" in text:
            matches.append({
                "site": "predictz",
                "raw": text
            })

    return matches
