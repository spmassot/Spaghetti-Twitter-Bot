import google_language as gl
from pytest import fixture


@fixture
def test_text():
    return (
        'Making America safe is my number one priority.'
        'We will not admit those into our country we cannot safely vet.'
    )


def test_get_sentiment(test_text):
    assert gl.get_sentiment(test_text) == (0, 0)


def test_get_entities(test_text):
    assert gl.get_entities(test_text) == {
        'safe': 'OTHER',
        'America': 'LOCATION',
        'priority.': 'OTHER',
        'country': 'LOCATION',
    }
