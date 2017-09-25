import tweepy
import os

def give_me_auth():
    auth = tweepy.OAuthHandler(
        os.environ['consumer_key'],
        os.environ['consumer_secret'])
    auth.set_access_token(
        os.environ['access_token'],
        os.environ['access_token_secret'])
    api = tweepy.API(auth)
    return api

def give_me_auth_too():
    auth = tweepy.OAuthHandler(
        os.environ['consumer_key'],
        os.environ['consumer_secret'])
    auth.set_access_token(
        os.environ['access_token'],
        os.environ['access_token_secret'])
    return auth


if __name__ == "__main__":
    api = give_me_auth()
    api.update_status('Hello Big Meatball!')
