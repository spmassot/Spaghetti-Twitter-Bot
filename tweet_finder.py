import tweepy
from auth import give_me_auth as auth

def tweet_finder():
    tweetr = tweepy.Cursor(
        auth().user_timeline,
        id='@realDonaldTrump',
        count=1
    ).items(1)
    return [x for x in tweetr][0]

if __name__ == '__main__':
    twt = tweet_finder()
    print(twt.text)
    print(twt.id)
