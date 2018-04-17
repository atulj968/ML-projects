"""
This program grabs the tweets form the twitter. You'll need your keys in order to grab that dta...
By use of tweepy I am acessing the twitter data and then I am extracting the username and their tweets!
By use of textblob(python library) I am doing the sentiment analysis of each tweet!
At last I am appening the results to a csv file with headers!


If you want to try this epic shit, just go to apps.twitter.com, and their sign up for twitter developers api, get your keys
and paste them here!
and then just run the program! boom! Thats it!
"""

from textblob import TextBlob
import tweepy
import numpy as np
import csv

consumer_key = "YOUR CONSUMER KEY HERE!"
consumer_key_secret = "YOUR CONSUMER KEY SECRET HERE"

acess_token = "YOUR ACESS TOKEN HERE"
acess_token_secret = 'YOUR ACESS TOKEN SECRET HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(acess_token, acess_token_secret)

api = tweepy.API(auth)

tweet_search_context = input("Enter the hot word for which you want to know the current sentiment in the world!\n")

public_tweets = api.search(tweet_search_context)

ds = []
with open('twitter_sentiment_analysis.csv', 'w', newline = '') as csvfile:
			fieldnames = ['username', 'tweet', 'sentiment_analysis_polarity']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()

for tweet in public_tweets:
	tweet_text = tweet.text
	username = ''
	print (tweet_text)
	temp = tweet_text.split('@', 1)
	if len(temp) > 1:
		temp2 = temp[1].split(' ')
		temp3 = temp2[0].split(':')
		username = temp3[0]
		u_tweet = " ".join(temp2[1:])
		analysis = TextBlob(tweet_text)

		with open('twitter_sentiment_analysis.csv', 'a', newline = '') as csvfile:
			fieldnames = [username, u_tweet, analysis.sentiment.polarity]
			writer = csv.writer(csvfile)
			writer.writerow(fieldnames)

print("Please checkout csv file created!")