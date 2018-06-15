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

file = open("../data/ids_tweets_recolectados_x_benja.txt","w")
file2 = open("../data/nombres_tweets_recolectados_x_benja.txt","w")

tweets = api.search(q="place:%s" % place_id)

for i in range(80):

	for tweet in tweets:
		print(tweet.id)
		print(tweet.user.screen_name)
		print("\n")
		file.write(str(tweet.id))
		file.write("\n")
		file2.write(tweet.user.screen_name)
		file2.write("\n")
		
	time.sleep(10)
	print(str(i / 80 * 100) + "%")


file.close()
file2.close()