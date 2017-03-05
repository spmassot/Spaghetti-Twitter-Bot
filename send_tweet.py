import tweepy
from auth import give_me_auth as auth
from maketweet import main as mktwt

def main(in_tweet):
    api = auth()
    api.update_status(mktwt(in_tweet))

if __name__ == '__main__':
    print(main('YA BOOBAY!'))
