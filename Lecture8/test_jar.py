from .jar import Jar

def test():
    jar = Jar()
    assert str(jar) == ""
def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == "🍪🍪"

def tset_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5