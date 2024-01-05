from unittest import mock
import random


def losowosc(p):
    return random.random() > p


@mock.patch('random.random')
def test_losowy(mock_random):
    mock_random.return_value = 0.1
    assert losowosc(0.0)
    assert not losowosc(0.1)
    assert mock_random.call_count == 2


def test_losowy2():
    with mock.patch('random.random') as mock_random:
        mock_random.return_value = 0.1
        assert losowosc(0.0)
        assert not losowosc(0.1)
        assert mock_random.call_count == 2