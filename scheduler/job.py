def run_job():
    print("🚀 START JOB")

    from scrapers.statarea import scrape_statarea
    from scrapers.betwizad import scrape_betwizad
    from scrapers.sportytrader import scrape_sportytrader
    from scrapers.predictz import scrape_predictz

    from core.parser import parse_match
    from core.probability_engine import compute_probability
    from bot.telegram_bot import send

    # ================= SCRAPING =================
    raw_data = []

    for func in [
        scrape_statarea,
        scrape_betwizad,
        scrape_sportytrader,
        scrape_predictz
    ]:
        try:
            data = func()
            print(f"✅ {func.__name__} → {len(data)}")
            raw_data += data
        except Exception as e:
            print(f"❌ {func.__name__} ERROR:", e)

    print("📥 TOTAL RAW:", len(raw_data))

    # ================= PARSING =================
    parsed = []

    for item in raw_data:
        try:
            parsed_item = parse_match(item["raw"])
            parsed.append(parsed_item)
        except Exception as e:
            print("❌ PARSE ERROR:", e)

    print("📊 PARSED:", len(parsed))

    # ================= DEBUG PARSED =================
    for p in parsed[:5]:
        print("➡️", p)

    # ================= PROBA =================
    results = compute_probability(parsed)

    print("🎯 RESULTS:", len(results))

    for r in results[:5]:
        print("🔥", r)

    # ================= TELEGRAM =================
    if not results:
        send("❌ DEBUG: Aucun résultat")
    else:
        msg = "🔥 DEBUG MATCHS\n\n"
        for match, prob in results[:5]:
            msg += f"{match} → {round(prob*100,2)}%\n"

        send(msg)

    print("✅ END JOB")
