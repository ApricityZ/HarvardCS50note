from hello import hello


def test_hello():
    assert hello("David") == "hello, David"
    assert hello() == "hello, World"


def test_default():
    assert hello() =="hello, World"