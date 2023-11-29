# from calculator import square
#
#
# def main():
#     testSquare()
#
#
# def testSquare():
#     # if square(2) != 4:
#     #     print("w square was not 4")
#     # if square(3) != 9:
#     #     print("3 squared was not 9")
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 square was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 square was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 square was not 0")
#
#
# """
#     test for more times!!!
#     but, we found the code in test is more than the tested code, to fix it,
#     use keyword: **assert**
#     but the code is still so much
#
#     **pytest** will relive it.
#     let's remake!
# """
#
# if __name__ == '__main__':
#     main()
import pytest

from calculator import square

def testpositive():
    assert square(2) == 4
    assert square(3) == 9
def testNegitive():
    assert square(-2) == 4
def testZero():
    assert square(0) == 0

"""
如果用户恶意输入怎么测试？
"""
    # assert square("cat") ==
"""
注意到，测试出错误时，剩下的测试不会继续进行，所以可以按照类型进行测试
"""
def tsetStr():
    with pytest.raises(TypeError):
        square("cat")