
import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import json
import requests
from bs4 import BeautifulSoup


def tweet(text: str):
    load_dotenv()
    consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
    consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
    access_token = os.environ.get("TWITTER_ACCES_TOKEN")
    access_token_secret = os.environ.get("TWITTER_ACCES_TOKEN_SECRET")

    payload = {"text": text}

    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )


def getTrends(number: int) -> list[str]:

    url = 'https://trends24.in/germany/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    trend_elements = soup.find_all('li')
    trends = []

    for element in trend_elements:
        trend = element.text.strip()
        
        if (trend[0] != "$"):
            trends.append(trend)

    return trends[:number]

