import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_html(url):
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Accept-Language": "en-US,en;q=0.9"
    }

    res = requests.get(url, headers=headers, timeout=15)
    return res.text


def scrape_betwizad():
    url = "https://betwizad.com/predictions"
    html = get_html(url)

    soup = BeautifulSoup(html, "lxml")

    matches = []

    # TABLE PRINCIPALE
    rows = soup.select("table tr")

    for row in rows:
        cols = row.find_all("td")

        if len(cols) < 2:
            continue

        try:
            time = cols[0].get_text(strip=True)

            # MATCH FORMAT: Arsenal -:- Everton
            match_text = cols[1].get_text(" ", strip=True)

            # TIP (1 / 2 / GG / Over etc)
            tip = cols[-3].get_text(strip=True)

            htft = cols[-2].get_text(strip=True)
            score = cols[-1].get_text(strip=True)

            matches.append({
                "site": "betwizad",
                "time": time,
                "match": match_text,
                "tip": tip,
                "htft": htft,
                "score": score
            })

        except Exception as e:
            continue

    return matches
