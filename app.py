import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

import tweet

# Initialization of flask app
app = Flask(__name__)

# like tweets scheduled for every 15 mins
scheduler = BackgroundScheduler()
scheduler.add_job(
    func=tweet.like_tweets,
    start_date="2022-04-19 20:30:00",
    trigger="interval",
    minutes=15,
)
scheduler.add_job(
    func=tweet.tweet_quote,
    start_date="2022-04-19 20:35:00",
    trigger="interval",
    hours=12,
)
scheduler.add_job(
    func=tweet.tweet_stats,
    start_date="2022-04-19 20:50:00",
    trigger="interval",
    hours=2,
)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    app.run()
