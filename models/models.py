from pynamodb.models import Model
from pynamodb.attributes import NumberAttribute

class TweetLog(Model):
    """A snapshot of the most recent tweet."""
    class Meta:
        table_name = 'tweet_log'
        region = 'us-east-1'
        read_capacity_units = 1
        write_capacity_units = 1

    last_tweet_id = NumberAttribute(hash_key=True)

def update_tweet(new_tweet_id):
    if not TweetLog.exists():
        TweetLog.create_table()

    last_tweet = [x for x in TweetLog.scan()]

    if not last_tweet:
        last_tweet = TweetLog(new_tweet_id)
        last_tweet.save()
    else:
        last_tweet[0].delete()
        last_tweet = TweetLog(new_tweet_id)
        last_tweet.save()

    return get_last_tweet()

def get_last_tweet():
    if not TweetLog.exists():
        return 0
    else:
        return [x.last_tweet_id for x in TweetLog.scan()][0]

if __name__ == '__main__':
    print(update_tweet(0))
    print(update_tweet(1))
    print(update_tweet(2))