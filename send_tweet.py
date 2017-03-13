import re
import tweepy
from auth import give_me_auth as auth
from maketweet import main as mktwt

def main(in_tweet):
    api = auth()
    new_twt = mktwt(in_tweet)
    url = re.compile("http.+(\s|$)")
    try:
        strt = url.search(new_tweet).start()
    except:
        strt = 0

    if len(new_twt) - strt > 135:
        api.update_status(new_twt[:135])
        api.update_status(new_twt[135:])
    else:
        api.update_status(new_twt)

if __name__ == '__main__':
    print(main('Ya Boobay'))
