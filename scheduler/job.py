def run_job():
    print("🚀 START JOB")

    from scrapers.statarea import scrape_statarea
    from scrapers.betwizad import scrape_betwizad
    from scrapers.sportytrader import scrape_sportytrader
    from scrapers.predictz import scrape_predictz

    from core.parser import parse_match
    from core.probability_engine import compute_probability
    from bot.telegram_bot import send

    # =========================
    # SCRAPING
    # =========================
    raw_data = []  # ✅ OBLIGATOIRE

    scrapers = [
        scrape_statarea,
        scrape_betwizad,
        scrape_sportytrader,
        scrape_predictz
    ]

    for func in scrapers:
        try:
            data = func()
            print(f"✅ {func.__name__}: {len(data)}")
            raw_data += data
        except Exception as e:
            print(f"❌ {func.__name__}:", e)

    print("📥 TOTAL RAW:", len(raw_data))

    # =========================
    # PARSING
    # =========================
    parsed = []

    for item in raw_data:
        try:
            parsed.append(parse_match(item["raw"]))
        except Exception as e:
            print("❌ PARSE:", e)

    parsed = [p for p in parsed if p["home"] and p["away"]]

    print("📊 PARSED:", len(parsed))

    # =========================
    # PROBA
    # =========================
    results = compute_probability(parsed)

    print("🎯 RESULTS:", len(results))

    # =========================
    # TELEGRAM
    # =========================
    if not results:
        send("❌ DEBUG: Aucun résultat")
    else:
        msg = "🔥 MATCHS\n\n"
        for match, prob in results[:5]:
            msg += f"{match} → {round(prob*100,2)}%\n"

        send(msg)

    print("✅ END JOB")
