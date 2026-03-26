def parse_betwizad(data):
    parsed = []

    for m in data:
        home, away = None, None

        if "-:-" in m["match"]:
            home, away = m["match"].split("-:-")

        parsed.append({
            "home": home.strip() if home else None,
            "away": away.strip() if away else None,
            "gg": "GG" in m["tip"],
            "over25": "Over 2.5" in m["tip"],
            "pick": m["tip"]
        })

    return parsed
