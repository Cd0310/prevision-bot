import re

def parse_match(text):
    match = {
        "home": None,
        "away": None,
        "gg": False,
        "over25": False,
        "pick": None
    }

    teams = re.split(r"vs|-", text)
    if len(teams) >= 2:
        match["home"] = teams[0].strip()
        match["away"] = teams[1].strip()

    if "GG" in text:
        match["gg"] = True

    if "Over 2.5" in text:
        match["over25"] = True

    if "1" in text:
        match["pick"] = "home"
    elif "2" in text:
        match["pick"] = "away"

    return match
