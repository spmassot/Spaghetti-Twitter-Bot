from google.cloud import language


def get_sentiment(in_text):
    language_client = language.Client()
    document = language_client.document_from_text(in_text)
    sentiment = document.analyze_sentiment().sentiment
    return (sentiment.score, sentiment.magnitude)


def get_entities(in_text):
    language_client = language.Client()
    document = language_client.document_from_text(in_text)
    response = document.analyze_entities()
    return {ent.name: ent.entity_type for ent in response.entities}
