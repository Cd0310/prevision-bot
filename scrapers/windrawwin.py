def scrape_windrawwin():
    url = "https://www.windrawwin.com/predictions/"
    
    try:
        html = get_html(url)
    except:
        return []

    soup = BeautifulSoup(html, "lxml")

    data = []

    for tr in soup.find_all("tr"):
        text = tr.get_text(" ", strip=True)

        if "vs" in text.lower():
            data.append({
                "site": "windrawwin",
                "raw": text
            })

    return data
