import sys
from datetime import date
import inflect


class CountMinus:
    def __init__(self,birthday):
        self.birthday = birthday
        self.today = date.today()

    def check_birthday(self):
        try:
            birthday = date.fromisoformat(self.birthday)
            return birthday
        except ValueError:
            print("Invalid date")
            sys.exit(0)

    def count_diff_days(self):
        birth_ordinal = self.check_birthday().toordinal()
        today_ordinal = self.today.toordinal()  # 没必要这样子，多此一举了
        diff = today_ordinal - birth_ordinal
        return diff

    def count_diff_minus(self):
        return self.count_diff_days() * 24 * 60

    def __str__(self):
        p = inflect.engine()
        return f"{p.number_to_words(self.count_diff_minus())} minutes".replace(" and","").capitalize()


def main():
    user_input= input("Input your Birthday:").strip()
    diff_minutes = CountMinus(user_input)
    print(diff_minutes)


if __name__ == '__main__':
    main()
