import tweepy
from auth import give_me_auth as auth

def main():
    return tweepy.Cursor(
        auth().user_timeline,
        id='@realDonaldTrump',
        count=5
    ).items(5)

if __name__ == '__main__':
    print([x for x in main()][0].text)
