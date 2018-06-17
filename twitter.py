import tweepy
from textblob import TextBlob



consumer_key    = "FqdF94rdZ7dPN95HZs9nMXRW5"
consumer_select = "6LgVIjsO0f9MlOlkTCCVSg61PR7vhj3CeBRXr2eD6HWxFZgxdk"


access_token = "775355465979035653-7hfRTS0R3ELWxq4qrwILJ6VGUnIpvaK"
access_token_secret = "UkUoLWIGnIQWMdk0JTYEPTTiA5QjTT5MTXXTF7tzHlKB1"


auth = tweepy.OAuthHandler(consumer_key , consumer_select)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
