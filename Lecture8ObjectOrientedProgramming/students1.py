import sys


class Student:  # property methods
    def __init__(self, name, house):  # self give you a home to store data :), use house = None to be option
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod    #避免先有鸡还是先有蛋的问题，不需要先实例化对象才能调用类方法get()py
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get() # elegant!
    print(student)


if __name__ == '__main__':
    main()

# return a (tuple) {dict} [list]
# {dict} is more explict
# the method start with __ __ in class are many
# we can control attribute by using property of class
# class method
