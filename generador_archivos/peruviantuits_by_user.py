#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import hidden3
import csv
import time
import sys

secrets = hidden3.oauth()
consumer_key = secrets['consumer_key']
consumer_secret = secrets['consumer_secret']
token_key = secrets['token_key']
token_secret = secrets['token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)

api = tweepy.API(auth)

tuitsFile = open('../data/peruviantuits_by_user2.tsv', 'a')
usersFile = open('../data/users/blacklist_users_peruviantuits.tsv', 'r')
blacklistusersFile = open('../data/users/blacklist_users_peruviantuits2.tsv', 'w')
csvWriter = csv.writer(tuitsFile, delimiter='\t')


def writeTuit(tuit):
	tuitId = tuit.id
	tuitAuthor = tuit.user.screen_name
	tuitTimestamp = tuit.created_at
	tuitText = tuit.text.encode('utf-8', errors="ignore")
	tuitPlace = tuit.place
	if None != tuitPlace:
		tuitPlace = tuit.place.name
	else:
		tuitPlace = ''
	
	csvWriter.writerow([tuitId, tuitAuthor, tuitTimestamp, tuitText, tuitPlace])

connectionReply = 0
current_user = usersFile.readline().replace('\n', '')
totaltweets = 0
while current_user != '':
	print("Recolectando tweets de " + current_user)
	try:
		item = api.get_user(current_user)
		tweet_count = 0
		for status in tweepy.Cursor(api.user_timeline, id=current_user).items():
			tweet_count += 1
			writeTuit(status)
			if tweet_count > 50:
				totaltweets += 50
				print(totaltweets)
				break
	except:
		blacklistusersFile.write(current_user + '\n')
	current_user = usersFile.readline().replace('\n', '')
	time.sleep(1)


tuitsFile.close()
usersFile.close()
blacklistusersFile.close()