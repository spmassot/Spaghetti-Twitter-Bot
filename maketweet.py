import re
import tweepy
from itertools import cycle
from google_language import get_entities

def tweet_maker(the_tweet):
    foods = cycle((
        'spaghetti',
        'meatballs',
        'marinara sauce',
        'steak pizzaiola',
        'baked ziti',
        'pecorino romano'
    ))
    the_new_tweet = the_tweet.text
    entities = get_entities(the_tweet.text)
    for word, entity_type in entities.items():
        the_new_tweet = the_new_tweet.replace(
            word,
            feed_me(
                next(foods),
                entity_type
        ))
    return replace_url(the_new_tweet)

def replace_url(in_string):
    url = re.compile("http.+(\s|$)")
    return url.sub(
        "https://www.youtube.com/watch?v=zWHu95io9B4 ",
        in_string
    )

def feed_me(subject, entity):
    return {
        'UNKNOWN':f'{subject}',
        'PERSON':f'the {subject} man',
        'LOCATION':f'{subject} city',
        'ORGANIZATION':f'The {subject.title()} Conservancy',
        'EVENT':f'{subject.title()} Day',
        'WORK_OF_ART':f'The {subject.title()} Lisa',
        'CONSUMER_GOOD':f'{subject}',
        'OTHER':f'{subject}'
    }.get(entity, f'{subject}')

if __name__ == '__main__':
    print(tweet_maker(input('Enter some text:')))

