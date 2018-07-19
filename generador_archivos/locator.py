import tweepy
import hidden
import csv
import time
import json

secrets = hidden.oauth()
consumer_key = secrets['consumer_key']
consumer_secret = secrets['consumer_secret']
token_key = secrets['token_key']
token_secret = secrets['token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)

api = tweepy.API(auth)
pais = input("¿Qué país buscás, che?\n")

places = api.geo_search(query=pais, granularity="country")
coords = places[0].bounding_box.coordinates[0]
nw = coords[0]
se = coords[2]

print("[{}, {}, {}, {}]".format(nw[0], nw[1], se[0], se[1]))
