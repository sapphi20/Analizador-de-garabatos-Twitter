#!/usr/bin/python
import json

with open('2000_tweets.json') as f:
    t = json.load(f)
file1 = open("un_tweet.json", "w")
file1.write(str(t[0]))
file1.close()    
#print(t[i]['text'])

