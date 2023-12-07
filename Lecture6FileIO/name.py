# names = []
#
# for _ in range(3):
#     names.append(input("What's your name? "))
#
# for name in names:
#     print(f"hello, {name}")
#

# to save what we input, use the file I/O
# first keywords: **open**

"""
name = input("What's your name? ")

file = open("names.txt", "a")   # the sceond param will decision the way we deal with the file "names.txt"
file.write(f"{name}\n")
file.close()
"""

# right now, if we repeat excute the name.py, we'll found only one name was saved.
# why?

# then we found the format is not we want, no new line.


# so far, it seems work in the way we hoped. but we may forget to **close** the file, so try the below code:
# key word: with open() as file:

# name = input("What's your name?")
#
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# then how can we read the data in the file?

# with open("names.txt", "r") as file:
#     lines = file.readlines()
#
# for line in lines:
#     print(f"hello, {line.rstrip()}")
#     # print("hello", line.rstrip())


# with open("names.txt", "r") as file:
#     for line in file:
#         print(f"hello, {line.rstrip()}")



# names = []  # creat a list to sort easily
#
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip()) # add data to the list
#
# for name in sorted(names):  # sort the list contains all data
#     print(f"hello, {name}")


# simplify the above code
# with open("names.txt") as file:
#     for line in sorted(file):   # sort the file directly, read document
#         print(f"hello, {line.rstrip()}")


# waht if i need store more information?
# the answer is to use the file type: **csv**
