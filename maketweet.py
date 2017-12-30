import re
import tweepy
from itertools import chain
from random import choice
from google_language import get_entities
from models.corpus import update_corpus


def tweet_maker(the_tweet):
    entities = get_entities(the_tweet)
    the_new_tweet = the_tweet
    for word, etype in entities.items():
        if word == '&amp':
            continue
        # update_corpus(word, etype)
        if '@' in word:
            continue
        combos = list(chain.from_iterable(
            [feed_me(food, word, etype) for food in get_foods()]
        ))
        replacer = min(combos, key=lambda x: abs(len(x) - len(word)))
        the_new_tweet = the_new_tweet.replace(word, replacer)
    return replace_url(the_new_tweet)


def replace_url(in_string):
    url = re.compile("http.+(\s|$)")
    return url.sub(
        "https://www.youtube.com/watch?v=zWHu95io9B4 ",
        in_string
    )


def get_foods():
    return [
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
    ]


def feed_me(food, origin, entity):
    return {
        'UNKNOWN': lambda food, orig: [orig],
        'PERSON': lambda food, orig: (
            [x.title() for x in [ f'{food} man', f'{food}', orig, ]]
            if orig.title() == orig
            else [ f'{food} man', f'{food}', orig, ]
        ),
        'LOCATION': lambda food, orig: (
            [x.title() for x in [ f'{food} land', f'{food} city', ]]
            if orig.title() == orig
            else [ f'{food} land', f'{food} city', ]
        ),
        'ORGANIZATION': lambda food, orig: [
            f'{food.title()} Conservancy',
            f'Department of {food.title()}',
            f'{food.title()} Association',
        ],
        'EVENT': lambda food, orig: [
            f'{food.title()} Day',
            f'war of {food.title()}',
        ],
        'WORK_OF_ART': lambda food, orig: [orig],
        'CONSUMER_GOOD': lambda food, orig: [f'{food}'],
        'OTHER':lambda food, orig: [ orig, f'{food}', f'{food}', ],
        }.get(entity, lambda food, orig: f'{food}')(food, origin)

if __name__ == '__main__':
    print(tweet_maker(input('Enter some text:')))

