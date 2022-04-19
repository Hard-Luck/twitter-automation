import csv
import random

import tweepy

import config
from btc import get_price

API_KEY = config.API_KEY
API_SECRET = config.API_SECRET
BEARER = config.BEARER
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_SECRET = config.ACCESS_SECRET

# Initialization of client
client = tweepy.Client(
    bearer_token=BEARER,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET,
    return_type=dict,
)
index = 1
get_ticker = index % 5
# List of cryptos to get info for crypt
tickers = [
    "BTC",
    "ETH",
    "FTM",
    "AVAX",
    "APE",
]
quotes = []

with open("Quotes.txt") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for line in reader:
        # Append list to list of lists
        quotes.append([line["QUOTE"], line["AUTHOR"]])


def like_tweets():
    tweets = client.search_recent_tweets(
        query="#FTM OR #NFT OR @boredapey -ass -dick -porn -sex -MangaMon",
        tweet_fields=["attachments"],
        max_results=20,
    )
    tweets_to_like = []
    for tweet in tweets["data"]:
        tweets_to_like.append(tweet["id"])
    try:
        for to_like in tweets_to_like:
            client.like(int(to_like))
        print("Successful")
    except:
        print("Unsuccessful")


def tweet_quote() -> None:
    """Takes random quote from csv file and tweets it"""
    random_number = int(random.randint(0, len(quotes) - 1))
    quote = f"{quotes[random_number][0]} - {quotes[random_number][1]}"
    while len(quote) > 288:
        quote = f"{quotes[random_number][0]} - {quotes[random_number][1]}\n#Inspirational #Quote #Goodday"
    client.create_tweet(text=quote)


def tweet_stats(ticker: str = tickers[get_ticker]) -> None:
    """Gets price of ticker, from list if not specified and tweets formatted message"""
    message = get_price(ticker)
    client.create_tweet(text=message)
    # Using global index to increment through tickers
    global index
    index += 1
