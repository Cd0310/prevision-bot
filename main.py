import schedule
import time
from scheduler.job import run_job

print("🤖 Bot démarré...")

# Exécution chaque jour à 10h
schedule.every().day.at("10:00").do(run_job)

# TEST (optionnel)
# schedule.every(1).minutes.do(run_job)

while True:
    schedule.run_pending()
    time.sleep(60)
