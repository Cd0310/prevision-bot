weights = {
    "statarea": 1.2,
    "soccervista": 1.0,
    "windrawwin": 1.1,
    "betwizad": 1.3,
    "sportytrader": 1.1,
    "predictz": 1.0,
    "winflix": 1.2
}

def compute_probability(matches):
    grouped = {}

    for m in matches:
        key = f"{m['home']} vs {m['away']}"

        if key not in grouped:
            grouped[key] = {"votes": 0, "gg": 0, "over25": 0, "home": 0, "away": 0}

        grouped[key]["votes"] += 1

        if m["gg"]:
            grouped[key]["gg"] += 1

        if m["over25"]:
            grouped[key]["over25"] += 1

        if m["pick"] == "home":
            grouped[key]["home"] += 1

        if m["pick"] == "away":
            grouped[key]["away"] += 1

    results = []

    for k, v in grouped.items():
        total = v["votes"]

        prob = max(
            v["gg"]/total,
            v["over25"]/total,
            v["home"]/total,
            v["away"]/total
        )

        if prob >= 0.40:  # ⚠️ ajusté réaliste
            results.append((k, prob))

    return results
