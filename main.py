import schedule
import time
import http.server
import socketserver
import threading

# Petit serveur pour tromper Render
def run_server():
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 10000), handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

from scheduler.job import run_job

print("🤖 Bot démarré...")

# Exécution chaque jour à 9h30h
schedule.every().day.at("14:15").do(run_job)

# TEST (optionnel)
# schedule.every(1).minutes.do(run_job)

while True:
    schedule.run_pending()
    time.sleep(60)
