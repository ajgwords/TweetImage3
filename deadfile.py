# -*- coding: utf-8 -*-
import tweepy

from time import sleep
import sys

consumer_key = "8hkACon4cweRON6LCHWRb1O2F"
consumer_secret = "GWkagEJGOs0uWbrGcw9UGqPnMX2dHcSSmmullnuhfcuHQLIhWi"
access_token ="4309565733-p6YC7u0o2OYnQvUeyAUR1nvsEKx8MxqL2iciraG"
access_token_secret = "EZHXgBgdbEJS4sS6ptjEHDsFLE7Q9hoyq6zPsNhU0ydGI"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

image = "/home/al/Pictures/SREF.png"
message = "This is an automated tweet sent using Tweepy"

api.update_with_media(image, status=message)
