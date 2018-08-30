import re
from os import getenv
import string
from itertools import chain
from random import choice
from google_language import get_entities
from models.corpus import update_corpus, update_count


def tweet_maker(the_tweet):
    entities = get_entities(the_tweet)
    the_new_tweet = the_tweet
    the_string = the_tweet.translate(
        str.maketrans('', '', string.punctuation)
    ).split()
    update_count(the_string)
    update_count(
        [f'{the_string[i - 1]} {x}' for i, x in enumerate(the_string)][1]
    )
    for word, etype in entities.items():
        if word == '&amp':
            continue
        update_corpus(word, etype)
        if '@' in word:
            continue
        combos = list(chain.from_iterable(
            [feed_me(repl, word, etype) for repl in get_repls()]
        ))
        replacer = choice(combos)
        the_new_tweet = the_new_tweet.replace(word, replacer)
        the_new_tweet = the_new_tweet.replace('&amp', '&')
    return replace_url(the_new_tweet)


def replace_url(in_string):
    url = re.compile("http.+(?=\s|$)")
    return url.sub(
        "https://www.youtube.com/watch?v=zWHu95io9B4 ",
        in_string
    )


def get_repls():
    return getenv('REPLACEMENTS').split(',')


def feed_me(repl, origin, entity):
    return {
        'UNKNOWN': lambda repl, orig: [orig],
        'PERSON': lambda repl, orig: (
            [x.title() for x in [f'{repl} man', f'{repl}', orig, ]]
            if orig.title() == orig
            else [f'{repl} man', f'{repl}', orig, ]
        ),
        'LOCATION': lambda repl, orig: (
            [x.title() for x in [f'{repl} land', f'{repl} city', ]]
            if orig.title() == orig
            else [f'{repl} land', f'{repl} city', ]
        ),
        'ORGANIZATION': lambda repl, orig: [
            f'{repl.title()} Conservancy',
            f'Department of {repl.title()}',
            f'{repl.title()} Association',
        ],
        'EVENT': lambda repl, orig: [
            f'{repl.title()} Day',
            f'war of {repl.title()}',
        ],
        'WORK_OF_ART': lambda repl, orig: [orig],
        'CONSUMER_GOOD': lambda repl, orig: [f'{repl}'],
        'OTHER': lambda repl, orig: [orig, f'{repl}', f'{repl}', ],
    }.get(entity, lambda repl, orig: f'{repl}')(repl, origin)


if __name__ == '__main__':
    print(tweet_maker(input('Enter some text:')))
