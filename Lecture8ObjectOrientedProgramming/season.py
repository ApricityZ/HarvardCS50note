from datetime import date
import re
import sys
import inflect

def main():
    season = Season.get()
    print(season.get_age_minute())


class Season:
    def __init__(self, birth):
        self.birth = birth


    @classmethod
    def get(cls):
        birth = input("Date of Birth: ")
        if not re.search(r"^\d{4}-\d?\d-\d?\d$", birth):
            sys.exit("Invalid date.")

        return cls(birth)


    def count_lear_year(self, birthyear):
        year = birthyear
        now_year = int(date.today().year)
        count_lear = 0
        while year <= now_year:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
                count_lear = count_lear + 1
            year = year + 1
        return count_lear


    def covert2int(self):
        birthday = self.birth.split("-")
        birthday = tuple(map(int, birthday))
        if birthday[1] < 0 or birthday[1] > 12:
            sys.exit()
        if birthday[2] < 0 or birthday[2] > 31:
            sys.exit()
        return birthday


    def get_age_minute(self):
        birthday = self.covert2int()
        num_lear_year = self.count_lear_year(birthday[0])
        birthday = date(birthday[0], birthday[1], birthday[2])
        diff_age = date.today() - birthday

        diff_day = num_lear_year + int(diff_age.days)
        diff_min = diff_day * 24 * 60
        inf = inflect.engine()
        min2words = inf.number_to_words(diff_min)
        min2words = min2words.replace(" and", "").capitalize()
        return min2words + " minutes"

# todo




if __name__ == '__main__':
    main()