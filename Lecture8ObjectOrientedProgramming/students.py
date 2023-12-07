import sys
class Student:  # property methods
    def __init__(self, name, house):    # self give you a home to store data :), use house = None to be option
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name.")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house    # attention self._house

    # Setter
    @house.setter   # 当类第一次被初始化时，就会调用这个函数
    def house(self, house): # when use : self.house = "  ", "self.house = " wil tell python what to de
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house # attention self._house

def main():
    student = get_student()
    student._house = "Number Four, Privet Drive"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == '__main__':
    main()

# return a (tuple) {dict} [list]
# {dict} is more explict
# the method start with __ __ in class are many
# we can control attribute by using property of class
# class method
