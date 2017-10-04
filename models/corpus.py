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
    entity_type = UnicodeAttribute()
    count = NumberAttribute(default=0)


def update_corpus(new_word, entity_type):
    if not Corpus.exists():
        Corpus.create_table()

    try:
        existing_word = Corpus.get(new_word)
    except:
        new_record = Corpus(
            new_word,
            entity_type=entity_type,
        )
        new_record.save()
        return True
    else:
        existing_word.update(
            attributes={
                'count':{'value':1,'action':'ADD'},
        })
        return False


if __name__ == '__main__':
    print(update_corpus('test','OTHER'))
    print(update_corpus('test','OTHER'))
