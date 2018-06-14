import tweepy
import hidden

secrets = hidden.oauth()
consumer_key = secrets['consumer_key']
consumer_secret = secrets['consumer_secret']
token_key = secrets['token_key']
token_secret = secrets['token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)

# Place id obtenido por geo api. Extraído de /data/locations.json
place_id = "47a3cf27863714de"
tweets = api.search(q="place:%s" % place_id)
for tweet in tweets:
	print(tweet.text + " | " + tweet.place.name if tweet.place else "Undefined place")

