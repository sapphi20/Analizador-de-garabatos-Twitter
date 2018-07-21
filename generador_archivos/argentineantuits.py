import tweepy
import hidden2
import csv
import time

secrets = hidden2.oauth()
consumer_key = secrets['consumer_key']
consumer_secret = secrets['consumer_secret']
token_key = secrets['token_key']
token_secret = secrets['token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token_key, token_secret)

api = tweepy.API(auth)

tuitsFile = open('../data/argentineantuits.tsv', 'a')
csvWriter = csv.writer(tuitsFile, delimiter='\t')


def writeTuit(tuit):
    tuitId = tuit.id
    tuitAuthor = tuit.user.screen_name
    tuitTimestamp = tuit.created_at
    tuitText = tuit.text
    tuitPlace = tuit.place.name
    csvWriter.writerow([tuitId, tuitAuthor, tuitTimestamp, tuitText, tuitPlace])
    print("[{}, {}] <{}>: {}".format(tuitTimestamp, tuitPlace, tuitAuthor, tuitText))
    

#Override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if(status.place is not None):
            if(status.place.country == "Argentina"):
                writeTuit(status)
        else: print(str(status.id) + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def on_error(self, status_code):
        tuitsFile.close()
        print(str(status_code))

errorCounter = 0
connectionReply = 0
#connectionUp = True
while(True):
    try:
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(locations=[-73.572716, -55.116856, -53.641135, -21.778451])
        errorCounter+=1
        connectionReply = 0
    except KeyboardInterrupt:
        print("Shao ql loh vimo")
        break
    except:
        connectionReply+=1
        print(str(connectionReply) + "intento de conexión")
        if(connectionReply > 2):
            # connectionUp = False
            print("Excedido tiempo de conexión")
            break
        time.sleep(60)
        
