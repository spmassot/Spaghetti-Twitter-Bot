import tweepy
from send_tweet import main as sendr
from auth import give_me_auth as auth

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        sendr(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=auth().auth, listener=myStreamListener)
myStream.filter(follow=['@realDonaldTrump'])

