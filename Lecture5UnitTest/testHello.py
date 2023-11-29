from hello import hello


def testDafault():
    assert hello() == "hello, world"
def testHello():
    assert hello("David") == "hello, David"
    # 由于hello函数并没有return任何东西，所以现在是无法测试的；为了解决这点，将 print 换为 return ，避免side effect，使程序可以测试

    # 每个测试函数应该尽可能的简单，宗旨是：keeping tests nice and simple is really the goalce