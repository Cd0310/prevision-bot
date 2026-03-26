import re

def parse_sportytrader(text):
    match = {
        "home": None,
        "away": None,
        "prob": 0,
        "pick": None
    }

    # équipes
    teams = re.split(r"-", text)
    if len(teams) >= 2:
        match["home"] = teams[0].strip()
        match["away"] = teams[1].strip()

    # probabilité
    prob = re.findall(r"(\d+)%", text)
    if prob:
        match["prob"] = int(prob[-1]) / 100

    # pick
    if "1" in text:
        match["pick"] = "home"
    elif "2" in text:
        match["pick"] = "away"

    return match
