#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import hidden
import time

secrets = hidden.oauth()
consumer_key = secrets['consumer_key']
consumer_secret = secrets['consumer_secret']
token_key = secrets['token_key']
token_secret = secrets['token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)

api = tweepy.API(auth)

# Place id obtenido por geo api. Extraído de /data/locations.json
place_id = "47a3cf27863714de"

file = open("../data/tweets_recolectados_x_benja.txt","w")

for i in range(4):
	tweets = api.search(q="place:%s" % place_id)
	for tweet in tweets:
		file.write(emoji.demojize(tweet.text) + " | " + tweet.place.name if tweet.place else "Undefined place")
		file.write("\n")
	
	time.sleep(10)
	print(str((i+1)*5) + " segundos")
	
file.close()