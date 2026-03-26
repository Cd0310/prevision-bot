import re

def parse_predictz(text):
    match = {
        "home": None,
        "away": None,
        "prob": 0,
        "pick": None,
        "gg": False,
        "over25": False
    }

    # équipes
    if "vs" in text:
        parts = text.split("vs")
        match["home"] = parts[0].strip()
        match["away"] = parts[1].strip()

    # probabilité %
    prob = re.findall(r"(\d+\.\d+)%", text)
    if prob:
        match["prob"] = float(prob[0]) / 100

    # règles
    if "Over 2.5" in text:
        match["over25"] = True

    if "GG" in text:
        match["gg"] = True

    if "1" in text:
        match["pick"] = "home"
    elif "2" in text:
        match["pick"] = "away"

    return match
