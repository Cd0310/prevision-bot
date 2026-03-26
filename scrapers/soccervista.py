def scrape_soccervista():
    url = "https://www.soccervista.com/"
    
    try:
        html = get_html(url)
    except:
        return []

    soup = BeautifulSoup(html, "lxml")

    matches = []

    for a in soup.find_all("a"):
        text = a.get_text(" ", strip=True)

        if "vs" in text.lower():
            matches.append({
                "site": "soccervista",
                "raw": text
            })

    return matches
