#! /usr/bin/env python3
"""Spaghetti-Twitter-Bot/Flask/Zappa."""

import tweepy
from tweepy.error import TweepError
from auth import give_me_auth as auth
from send_tweet import main as send_tweet
from tweet_finder import tweet_finder as finder
from models.tweetlog import get_last_tweet, update_tweet_log


def check_go(in_tweet):
    if in_tweet.id > get_last_tweet():
        return True
    else:
        return False

def main():
    new_tweet = finder()
    if check_go(new_tweet):
        try:
            send_tweet(new_tweet)
        except TweepError:
            update_tweet_log(new_tweet.id)
        else:
            update_tweet_log(new_tweet.id)
    else:
        return

if __name__ == '__main__':
    main()

