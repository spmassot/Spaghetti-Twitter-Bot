import re
import os
import requests

def main(in_word):
    """Returns a tuple containing (word,part of speech)"""
    return get_pos(request_builder(in_word).text) == 'Noun'   

def request_builder(word):
    """Takes an input word, hits the dictionary api, and returns a response object."""
    url = 'https://od-api.oxforddictionaries.com/api/v1'
    route = '/entries'
    full = url+route+'/en/'+word.lower()
    return requests.get(full,
                        headers={'app_id':os.environ['dict_app_id'],
                                 'app_key':os.environ['dict_app_key']})

def get_pos(in_blob):
    """Takes a json blob and returns just the part of speech"""
    pos_match = re.compile("lexicalCategory\":\s*\"(?P<partOfSpeech>[a-zA-Z]+)")
    try:
        return pos_match.search(in_blob).groupdict()['partOfSpeech']
    except:
        return 'Noap'
    
if __name__ == '__main__':
    print([main(x) for x in ['tree','baseball','kick','heavy','USA','AMERICA']])
