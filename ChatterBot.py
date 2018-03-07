# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "GRBtjRLdCxgFSBy9t7bUCRGbb"
consumer_secret = "hajaxM4STqQHK6jvSyd0z6E2RhhA3pYlpyixkNdrobyaGbtOjw"
access_token = "859300194541752320-9gE7OdprsyPxQXLS0TZbZC2unEoZsDj"
access_token_secret = "K5hgSSDzxoMcWXxcOi78ZfCG2ZWvRCAeaM9mUz2fIpPIM"


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
