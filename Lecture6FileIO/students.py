# with open("students.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         # to make the code more readable
#         name, house = line.rstrip().split(",")  # automatically allocate to two variable: name and house
#         print(f"{name} is in {house}")


# sort by name:
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
#
# for student in sorted(students):
#     print(student)

# even the above code realize we want, but it seems not a good way to construct senteces and sort them
# craete a dictionary
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
# for student in students:
#     print(f"{student['name']} is in {student['house']}")


# if we want sort by name, we can not deirectly use: sorted(students) since students is a dict.
# luckily, there is a param named **key** in sorted function, which indicate the basis of ranking

# def get_name(student):
#     return student["name"]


# for student in sorted(students, key=get_name):  # 函数可以作为参数进行传递,注意没有()
# 使用 lambda 语法可以创建匿名函数，省去 get_name function
# for student in sorted(students, key= lambda student: student["name"]):  # lambda 中的 keyword可以任意写
#     print(f"{student['name']} is in {student['house']}")

# 如果csv某行中有三个逗号，那么会报错

# 了解CSV library，不重复造轮子
# 在此处修改csv文件，

# import csv
# students = []
#
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#        students.append({"name":name, "home": home})
#
#
# for student in sorted(students, key= lambda student: student["name"]):  # lambda 中的 keyword可以任意写
#     print(f"{student['name']} is in {student['home']}")

# 事实上，可以在csv文件中的**第一行**添加信息，作为字典的 键 ， 然后使用DictReader，可以自动识别第一行为字典的键


#################################################
# 下面讨论如何写csv文件：
# import csv
#
# name = input("What's your name?")
# home = input("Where's your home?")
#
# with open("students.csv", "a") as file:
#     # writer = csv.writer(file)
#     # writer.writerow([name, home])
#     writer = csv.DictWriter(file,fieldnames=["name", "home"])
#     writer.writerow({"name":name, "home":home})


# use the Library "pillow"
