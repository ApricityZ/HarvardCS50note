import random


def get_num(promote: str) -> int:
    while True:
        num = input(promote)
        try:
            input_int = int(num)
        except ValueError:
            continue
        if input_int > 0:
            return input_int
        else:
            pass


pre_num = get_num("Level:")
pre_num = random.randint(1, pre_num)
while True:

    guess = get_num("Guess:")
    if guess == pre_num:
        print("Just right!")
        break
    elif guess < pre_num:
        print("Too small!")
        pass
    else:
        print("Too large!")
        pass
