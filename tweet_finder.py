import tweepy
import os
from auth import give_me_auth as auth

def main():
    api = auth()
    return tweepy.Cursor(api.user_timeline, id='@realDonaldTrump', count=1).items(1)

if __name__ == '__main__':
    main()
