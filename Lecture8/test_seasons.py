from .seasons import CountMinus

def test():
    result = CountMinus("2023-04-18")   # 如果类中使用`__str__`,那么要进行类型转换
    assert str(result) == "Five hundred twenty-seven thousand forty minutes"