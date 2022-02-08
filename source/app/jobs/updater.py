from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import make_expired


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(make_expired, 'interval', hours=24)
    scheduler.start()
