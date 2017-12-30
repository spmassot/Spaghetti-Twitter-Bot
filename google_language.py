from google.cloud import language


def get_sentiment(in_text):
    language_client = language.Client()
    document = language_client.document_from_text(in_text)
    sentiment = document.analyze_sentiment().sentiment
    return sentiment


def get_entities(in_text):
    language_client = language.Client()
    document = language_client.document_from_text(in_text)
    response = document.analyze_entities()
    return {ent.name:ent.entity_type for ent in response.entities}


if __name__ == '__main__':
    text= 'Making America safe is my number one priority.'
    'We will not admit those into our country we cannot safely vet.'
    entities = get_entities(text)
    print(entities)
