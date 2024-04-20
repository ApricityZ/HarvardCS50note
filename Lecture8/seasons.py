import sys
from datetime import date
import re
import inflect


class CountMinus:
    def __init__(self,birthday):
        self.birthday = birthday
        self.today = date.today()

    # @staticmethod
    def check_birthday(self):
        # birthday_input = input("Input your birthday:")
        # if matches := re.search(r"(\d+?)-(\d+?)-(\d+?)", birthday_input):
        #     try:
        #         return date(matches[0], matches[1], matches[2])
        #     except ValueError("Invalid input"):
        #         sys.exit(1)
        try:
            birthday = date.fromisoformat(self.birthday)
            return birthday
        except ValueError:
            # raise ValueError("Invalid input")
            print("Invalid date")
            sys.exit(0)
    # @staticmethod
    # def get_today():
    #     return date.today()

    def count_diff_days(self):
        birth_ordinal = self.check_birthday().toordinal()
        today_ordinal = self.today.toordinal()
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
    # minutes = diff_minutes.minus2word()
    print(diff_minutes)
    # print(CountMinus("2023-04-18"))


if __name__ == '__main__':
    main()
