from bank import value


def test_reght():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0


def test_twenty():
    assert value("How are you doing?") == 20


def test_forty():
    assert value("What's happending?") == 100