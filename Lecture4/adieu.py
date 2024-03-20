# import inflect
#
#
# def main():
#     global mylist
#     p = inflect.engine()  # 实例化类
#     name = []
#     while True:
#         try:
#             name.append(input("Name: ").strip())
#             mylist = p.join(name, final_sep="")
#         except EOFError:
#             print("Adieu, adieu, to {}".format(mylist))
#
#
# if __name__ == '__main__':
#     main()
import inflect

def get_name():
    p = inflect.engine()  # 实例化类
    name = []
    while True:
        try:
            name_str = input("Name: ").strip()
            name.append(name_str)
        except EOFError:
            break
    mylist = p.join(name, final_sep="")
    return mylist

def main():
    name = get_name()
    print("Adieu, adieu, to {}".format(name))

if __name__ == '__main__':
    main()