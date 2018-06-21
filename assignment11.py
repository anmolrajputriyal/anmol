#Q1
#An Access Token is an object that describes the security context of a process or thread.

#sign in to the developer account
#create a new API
#under that go to keys and access token
#generate access token

#Q2
#google ip address=172.216.15.67
#facebook ip address=31.11.67.227

#Q3
from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy
oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
print(api.search("#cricket"))

#Q4
#API can be written in any language.
#Library is written in same language which is a collection of all the functionalities required for the use case.
#for example: Numpy is a library of python,adding support for large,multi-dimensional arrays and matrices, along
    #with alarge collection of high level mathematical functions to operate on these array.

#Q5
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
consumer_key=""
consumer_secret=""
access_token=""
access_secret=""
class listener(StreamListener):
    def on_data(self,data):
        print(data)
        return True
    def on_error(selfself,status):
        print(status)
auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
twitterstream=Stream(auth,listener())
twitterstream.filter(track=["#cricket"])

