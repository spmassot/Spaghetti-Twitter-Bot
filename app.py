import re
import tweepy
from tweet_finder import main as twt

def transform_tweet():
    the_tweet = [x for x in twt()][0].text
    proper_nouns, nouns, urls = reg_defs()
    food = feed_me()
    do_not_replace = ['meatball','Meatball','spaghetti','marinara sauce']
    the_tweet = proper_nouns.sub("Big Mr. Meatball", the_tweet)
    the_tweet = urls.sub('https://www.youtube.com/watch?v=BKQGamvO_yM', the_tweet)
    print(the_tweet)
    no_nouns = [x for x in nouns.findall(the_tweet)]
    for xyz in [x[1] for x in no_nouns]:
        if xyz not in do_not_replace:
            the_tweet = the_tweet.replace(xyz, next(food))

    print(the_tweet)

def feed_me():
    while True:
        yield 'meatball'
        yield 'spaghetti'
        yield 'marinara sauce'
    
def reg_defs():
    proper_nouns = re.compile('(Trump|I|Me|me)')
    nouns = re.compile("""(the|in|of|this|these)\s(?P<replaceeone>[a-zA-Z]+)|
                          (?P<replacee>[a-zA-Z]+)\s(is|are|were|was|of)""",re.X)
    urls = re.compile("""[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)""")
    return proper_nouns, nouns, urls
    

transform_tweet()

