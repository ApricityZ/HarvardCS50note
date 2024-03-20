def main():
    str_input = input("camelCase: ")
    position_list = find_uppercase_position(str_input)
    convert_input = add_underscore(position_list, str_input)

    print(convert_input)


def find_uppercase_position(s):
    uppercase_position = []
    s = s.strip()
    for i in range(len(s)):
        if s[i].isupper():
            uppercase_position.append(i)

    return uppercase_position


def insert_char(s, index, char):
    return s[:index] + char + s[index:]


def add_underscore(l, s):
    s = s.lower()
    insert_count = 0
    # print("here")
    for i in range(len(l)):
        index = l[i] + insert_count
        s = insert_char(s, index, "_")
        insert_count += 1
        # if i == 0:
        #     insert_char(s, index,"_")
        # else:
        #     insert_char(s, index, "_")
# 如果索引需要持续更新，那么可以采用计数的方式（添加计数变量`count`），或者利用`for`循环中的索引`i`进行,宗旨是使用变量追踪变化.
    return s


if __name__ == '__main__':
    main()
