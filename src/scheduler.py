import schedule
import time

def notify(message):
    print(f"\n🔔 Lembrete: {message}\n")

def start_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)