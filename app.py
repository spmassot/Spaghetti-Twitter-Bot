import tweepy
from auth import give_me_auth as auth
from tweet_finder import tweet_finder as finder
from maketweet import tweet_maker

def tweet_finder():
    return tweepy.Cursor(
        auth().user_timeline,
        id='@realDonaldTrump',
        count=1
    ).items(1)

def
