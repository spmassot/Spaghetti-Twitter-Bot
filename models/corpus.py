from pynamodb.models import Model
from pynamodb.attributes import NumberAttribute, UnicodeAttribute


class Corpus(Model):
    """A word, its entity type, and usage statistics."""
    class Meta:
        table_name = 'corpus'
        region = 'us-east-1'
        read_capacity_units = 1
        write_capacity_units = 1

    word = UnicodeAttribute(hash_key=True)
    entity_type = UnicodeAttribute(default='None')
    count = NumberAttribute(default=0)


def update_corpus(new_word, entity_type):
    if not Corpus.exists():
        Corpus.create_table()

    try:
        Corpus.get(new_word)
    except Exception:
        new_record = Corpus(
            new_word,
            entity_type=entity_type,
        )
        new_record.save()
        return True


def update_count(word_or_words):
    if isinstance(word_or_words, list):
        return [update_count(word) for word in word_or_words]

    if not Corpus.exists():
        Corpus.create_table()
    try:
        existing_word = Corpus.get(word_or_words)
    except Exception:
        new_record = Corpus(word_or_words)
        new_record.save()
        return True
    else:
        existing_word.update(
            attributes={
                'count': {'value': 1, 'action': 'ADD'},
            }
        )
        return False


if __name__ == '__main__':
    import csv
    with open('corpus.csv', 'w') as csvf:
        corpus_writer = csv.writer(csvf)
        corpus_writer.writerow(['Word', 'Entity Type', 'Count'])
        for i in Corpus.scan():
            corpus_writer.writerow([i.word, i.entity_type, i.count])
