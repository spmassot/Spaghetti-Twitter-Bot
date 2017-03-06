import tweepy
from send_tweet import main as sendr
from auth import give_me_auth_too as auth

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.author.id_str == '25073877':
            print(status.text)
            try:
                sendr(status.text)
            except BaseException as e:
                print(e)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print('issue')
            #returning False in on_data disconnects the stream
            return False
        return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=auth(), listener=myStreamListener)
try:
    myStream.filter(follow=['25073877'])
except:
    myStream.filter(follow=['25074877'])
