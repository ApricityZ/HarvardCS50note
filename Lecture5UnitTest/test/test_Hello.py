import sys
sys.path.append("..")
from Lecture5UnitTest.hello import hello
# from hello import hello


def test_Dafault():
    assert hello() == "hello, world"
def test_Hello():
    assert hello("David") == "hello, David"



