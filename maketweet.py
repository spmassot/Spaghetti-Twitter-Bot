import re
import tweepy
from random import choice
from google_language import get_entities
from models.corpus import update_corpus

def tweet_maker(the_tweet):
    entities = get_entities(the_tweet)
    the_new_tweet = the_tweet
    for word, entity_type in entities.items():
        length = len(word)
        update_corpus(word, entity_type)
        the_new_tweet = the_new_tweet.replace(
            word, choice(feed_me(choice(get_foods())[0], word, entity_type))
        )
    return replace_url(the_new_tweet)

def replace_url(in_string):
    url = re.compile("http.+(\s|$)")
    return url.sub(
        "https://www.youtube.com/watch?v=zWHu95io9B4 ",
        in_string
    )

def get_foods():
    return [(x,len(x)) for x in (
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
    )]

def feed_me(food, origin, entity):
    return {
        'UNKNOWN':[
            origin,
        ],
        'PERSON':[
            f'{food} man',
            origin,
        ],
        'LOCATION':[
            f'{food} land',
            f'{food} city',
        ],
        'ORGANIZATION':[
            f'{food.title()} Conservancy',
            f'Department of {food.title()}',
            f'{food.title()} Association',
        ],
        'EVENT':[
            f'{food.title()} Day',
            f'war of {food.title()}',
        ],
        'WORK_OF_ART':[
            origin,
        ],
        'CONSUMER_GOOD':[
            f'{food}',
        ],
        'OTHER':[
            origin,
            f'{food}',
            f'{food}',
        ],
    }.get(entity, f'{food}')

if __name__ == '__main__':
    print(tweet_maker(input('Enter some text:')))

