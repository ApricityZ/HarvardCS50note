from datetime import date
import inflect

def main():
    season = Season.get()
    minutes = Season.get_old()


class Season:
    def __init__(self, birth):
        self.birth = birth


    @classmethod
    def get(cls):
        birth = input("Date of Birth: ")
        return cls(birth)


    def count_lear_year(self, birth):
        birth_year, _, _  = birth.split("-")
        year = int(birth_year)
        now_year = date.year
        count_lear = 0
        while year <= now_year:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
                count_lear = count_lear + 1
            year = year + 1
        return count_lear


    def __sub__(self, other):
        today = date.today()








if __name__ == '__main__':
    main()