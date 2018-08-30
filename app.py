#! /usr/bin/env python3
"""Spaghetti-Twitter-Bot/Flask/Zappa."""

from tweepy.error import TweepError
from send_tweet import main as send_tweet
from tweet_finder import tweet_finder as finder
from models.tweetlog import get_last_tweet, update_tweet_log
from logger import log


def main():
    new_tweet = finder()
    if new_tweet.id > get_last_tweet():
        try:
            send_tweet(new_tweet)
            log(new_tweet.id, new_tweet.text)
        except TweepError as e:
            update_tweet_log(new_tweet.id)
            log(new_tweet.id, e)
        else:
            update_tweet_log(new_tweet.id)
    else:
        log(new_tweet.id, 'has already been used.')
        return


if __name__ == '__main__':
    main()
