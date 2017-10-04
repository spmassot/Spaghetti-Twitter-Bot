import re
import tweepy
from random import choice
from itertools import cycle
from google_language import get_entities
from models.corpus import update_corpus

def tweet_maker(the_tweet):
    foods = cycle((
        'spaghetti',
        'meatballs',
        'marinara sauce',
        'steak pizzaiola',
        'baked ziti',
        'pecorino romano',
        'oregano',
        'basil',
        'mozzarella',
        'bolognese',
        'parmesean'
    ))
    the_new_tweet = the_tweet.text
    entities = get_entities(the_tweet.text)
    for word, entity_type in entities.items():
        update_corpus(word, entity_type)
        the_new_tweet = the_new_tweet.replace(
            word,
            choice(
                feed_me(next(foods), entity_type)
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
        'UNKNOWN':[
            f'{subject}',
            f'some kind of {subject}',
        ],
        'PERSON':[
            f'{subject} man',
        ],
        'LOCATION':[
            f'{subject} land',
            f'{subject} city',
        ],
        'ORGANIZATION':[
            f'{subject.title()} Conservancy',
            f'Department of {subject.title()}',
            f'{subject.title()} Association',
        ],
        'EVENT':[
            f'{subject.title()} Day',
            f'war of {subject.title()}',
        ],
        'WORK_OF_ART':[
            f'Mona {subject.title()}',
            f'Thinking {subject.title()}',
            f'{subject.title()} Descending a Staircase',
        ],
        'CONSUMER_GOOD':[
            f'{subject}',
        ],
        'OTHER':[
            f'{subject}',
        ],
    }.get(entity, f'{subject}')

if __name__ == '__main__':
    print(tweet_maker(input('Enter some text:')))

