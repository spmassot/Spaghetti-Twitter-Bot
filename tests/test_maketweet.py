import maketweet as mt


def test_tweet_maker():
    pass


def test_replace_url():
    pass


def test_get_foods():
    assert mt.get_foods() == [
        'spaghetti', 'meatballs', 'marinara sauce', 'steak pizzaiola',
        'baked ziti', 'pecorino romano', 'oregano', 'basil', 'mozzarella',
        'bolognese', 'parmesean', 'panettone', 'carbonara',
        'eggplant rolitini', 'ricotta', 'pepperoni'
    ]


def test_feed_me():
    food = 'spaghetti'
    test_a = 'sport'
    test_b = 'Sport'
    for z, k in (
        ('UNKNOWN', ['sport']),
        ('PERSON', ['spaghetti man', 'spaghetti', 'sport']),
        ('LOCATION', ['spaghetti land', 'spaghetti city']),
        ('ORGANIZATION', ['Spaghetti Conservancy',
                          'Department of Spaghetti',
                          'Spaghetti Association']),
        ('EVENT', ['Spaghetti Day', 'war of Spaghetti']),
        ('WORK_OF_ART', ['sport']),
        ('CONSUMER_GOOD', ['spaghetti']),
        ('OTHER', ['sport', 'spaghetti', 'spaghetti']),
    ):
        assert mt.feed_me(food, test_a, z) == k
    for z, k in (
        ('PERSON', ['Spaghetti Man', 'Spaghetti', 'Sport']),
        ('LOCATION', ['Spaghetti Land', 'Spaghetti City']),
    ):
        assert mt.feed_me(food, test_b, z) == k
