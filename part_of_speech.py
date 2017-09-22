import re
import os
import requests

def part_of_speech(in_word):
    """Returns a tuple containing (word,part of speech)"""
    return get_pos(
        request_builder(make_singular(in_word)).text
    ) == 'Noun'   

def request_builder(word):
    """Takes an input word, hits the dictionary api, 
    and returns a response object."""
    url = 'https://od-api.oxforddictionaries.com/api/v1'
    route = '/entries'
    full = url+route+'/en/'+word.lower()
    return requests.get(
        full,
        headers={
            'app_id':os.environ['dict_app_id'],
            'app_key':os.environ['dict_app_key']
    })

def get_pos(in_blob):
    """Takes a json blob and returns just the part of speech"""
    pos_match = re.compile("lexicalCategory\":\s*\"(?P<partOfSpeech>[a-zA-Z]+)")
    try:
        return pos_match.search(in_blob).groupdict()['partOfSpeech']
    except:
        return 'Noap'

def make_singular(in_word):
    plural_match = re.compile('([a-zA-Z]+?)(s$|es$|$)')
    try:
        return plural_match.search(in_word).group(1)
    except:
        return in_word
    
if __name__ == '__main__':
    print([main(x) for x in ['turkey','rats','tree','flying','sword','into']])
