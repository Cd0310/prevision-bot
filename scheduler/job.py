from scrapers.statarea import scrape_statarea
from scrapers.soccervista import scrape_soccervista
from scrapers.windrawwin import scrape_windrawwin
from scrapers.betwizad import scrape_betwizad
from scrapers.sportytrader import scrape_sportytrader
from scrapers.predictz import scrape_predictz
from scrapers.winflix import scrape_winflix

from core.parser import parse_match
from core.betwizad_parser import parse_betwizad

from core.probability_engine import compute_probability
from bot.telegram_bot import send


def run_job():
    print("🚀 Lancement scraping multi-sites...")

    raw_data = []

    # =========================
    # SCRAPING
    # =========================
    try:
        raw_data += scrape_statarea()
        print("✅ statarea OK")
    except:
        print("❌ statarea fail")

    try:
        raw_data += scrape_soccervista()
        print("✅ soccervista OK")
    except:
        print("❌ soccervista fail")

    try:
        raw_data += scrape_windrawwin()
        print("✅ windrawwin OK")
    except:
        print("❌ windrawwin fail")

    try:
        raw_data += scrape_betwizad()
        print("✅ betwizad OK")
    except:
        print("❌ betwizad fail")

    try:
        raw_data += scrape_sportytrader()
        print("✅ sportytrader OK")
    except:
        print("❌ sportytrader fail")

    try:
        raw_data += scrape_predictz()
        print("✅ predictz OK")
    except:
        print("❌ predictz fail")

    try:
        raw_data += scrape_winflix()
        print("✅ winflix OK")
    except:
        print("❌ winflix fail")

    # =========================
    # PARSING
    # =========================
    parsed = []

    for item in raw_data:
        try:
            # Betwizad a son parser spécifique
            if item["site"] == "betwizad":
                parsed += parse_betwizad([item])
            else:
                parsed.append(parse_match(item["raw"]))
        except:
            continue

    # Nettoyage (important)
    parsed = [
        p for p in parsed
        if p["home"] is not None and p["away"] is not None
    ]

    print(f"📊 Matchs valides: {len(parsed)}")

    # =========================
    # CALCUL PROBABILITÉ
    # =========================
    results = compute_probability(parsed)

    # =========================
    # TELEGRAM
    # =========================
    if not results:
        send("❌ Aucune prédiction fiable aujourd’hui (multi-sites)")
        return

    msg = "🔥 PRÉDICTIONS ULTRA FIABLES (IA + Multi-sites)\n\n"

    for match, prob in results:
        msg += f"⚽ {match}\n📊 {round(prob*100,2)}%\n\n"

    send(msg)

    print("✅ Message envoyé")
