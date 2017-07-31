import re
import tweepy
from part_of_speech import main as pos

def main(the_tweet):
    feeder = feed_me()
    the_new_tweet = ' '.join(
        [subber(x,feeder) if pos(x) else x 
        for x in the_tweet.split(' ')]
    )
    return replace_url(the_new_tweet)
    
def subber(inword, food):
    return next(food).upper() if inword.upper() == inword else next(food)

def replace_url(in_string):
    url = re.compile("http.+(\s|$)")
    return url.sub("https://www.youtube.com/watch?v=zWHu95io9B4 ", in_string)
    
def feed_me():
    while True:
        yield 'spaghetti'
        yield 'meatballs'
        yield 'marinara sauce'
        yield 'parmesan'
        yield 'spicy meatball'
	
if __name__ == '__main__':
    print(main(input('Enter some text:')))

