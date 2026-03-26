import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_html(url):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    return requests.get(url, headers=headers, timeout=10).text


def scrape_sportytrader():
    url = "https://www.sportytrader.com/en/betting-tips/"
    html = get_html(url)

    soup = BeautifulSoup(html, "lxml")

    data = []

    matches = soup.select("div")  # structure flexible

    for m in matches:
        text = m.get_text(" ", strip=True)

        # filtrage intelligent
        if "-" in text and "%" in text:
            data.append({
                "site": "sportytrader",
                "raw": text
            })

    return data
