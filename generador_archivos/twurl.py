import urllib
import oauth
import hidden

def augment(url, parameters) :
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'],secrets['token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, 
        token=token, http_method='GET', http_url=url, parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()


def get_last_n_tweets_from(n, user) :
    print '* Calling Twitter...'
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {'screen_name': user, 'count': str(n)} )
    connection = urllib.urlopen(url)
    data = connection.read()
	
    headers = connection.info().dict
    return data
	
def get_user(user):
	print '* Calling Twitter...'
	url = augment('https://api.twitter.com/1.1/users/show.json', {'screen_name': user})
	connection = urllib.urlopen(url)
	data = connection.read()
	
	headers = connection.info().dict
	return data
	
print(get_user("sapphi20"))