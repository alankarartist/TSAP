import tweepy
from textblob import TextBlob
from statistics import *
consumer_key = 'p5j8eNlzGO6l5sNsbhGJ3uqYq'
consumer_secret = 'PgUCqKrKnFcyHmbZSfEddjz69iZt2nRemMWh6Pa3yjbQoyd7Pg'
access_token = '777191106429628416-FpOqY2FRppfefZUZ8hSSvZmRMqDsjMg'
access_token_secret = 'pbIqFZ5c1bt3WxIEHlE5PPsvSbi6moU7NAcpz1j5MJPbi'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
subject = input('Enter the keyword that you want to search ')
list = []
neu=0
pos=0
neg=0
c =0
for tweet in tweepy.Cursor(api.search, q=subject).items(1000):
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    list.append(analysis.sentiment.polarity)
    c+=1
print ("Average Polarity" + str(mean(list)) )   
for i in list:
    if i==0.0:
       neu+=1
    if i>0.0:
       pos+=1
    if i<0.0:
       neg+=1
print ("Total Neutral :" + str(neu))
print ("Total Positive :" + str(pos))
print("Total Negative :" + str(neg))
print("Total Tweets Searched" + str(c))
