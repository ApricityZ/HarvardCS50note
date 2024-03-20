import random

def get_num(promote: str) -> int:
    while True:
        num = input(promote)
        if num.isdigit():  # 使用isdigit()方法检查输入是否为数字
            input_int = int(num)
            if input_int > 0:
                return input_int
        print("Please enter a positive integer.")

pre_num = get_num("Level:")
pre_num = random.randint(1, pre_num)

while True:
    guess = get_num("Guess:")
    if guess == pre_num:
        print("Just right!")
        break
    elif guess < pre_num:
        print("Too small!")
    else:
        print("Too large!")

"""主要改进包括：

使用isdigit()方法来检查用户输入是否为数字，这样可以避免异常处理，提高了效率。
减少了不必要的else子句，提高了代码的可读性。
移除了不必要的pass语句。"""