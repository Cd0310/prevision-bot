import requests

TOKEN = "8623082732:AAHoxYTdqTkRvDCxEms0jdEZNT2sS0peapc"
CHAT_ID = "6379592530"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    try:
        requests.post(url, data=data, timeout=10)
        print("✅ Telegram envoyé")
    except Exception as e:
        print("❌ Erreur Telegram:", e)
