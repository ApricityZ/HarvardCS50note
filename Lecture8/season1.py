import sys
from datetime import date
import inflect


class CountMinus:
    def __init__(self, birthday):
        self.birthday = birthday
        self.today = date.today()

    def check_birthday(self):
        try:
            return date.fromisoformat(self.birthday)    # 直接使用return简化代码
        except ValueError:
            raise ValueError("Invalid date")    # 使用raise来使程序更加的清晰


    def count_diff_minutes(self):
        return abs((self.today - self.check_birthday()).days * 24 * 60) # date 类型已经考虑过了闰年的问题

    def __str__(self):
        p = inflect.engine()
        return f"{p.number_to_words(self.count_diff_minutes())} minutes".replace(" and", "").capitalize()


def main():
    user_input = input("Input your Birthday:").strip()
    try:    # 在主函数中处理异常，在类或函数中只使用raise来引发错误
        diff_minutes = CountMinus(user_input)
        print(diff_minutes)
    except ValueError as e: # 注意后面的 as e， 这样可以打印出错误信息
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
