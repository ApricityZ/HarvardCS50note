def is_valid(s):
    s = s.strip()
    # 当需要返回Bool值时,不需要使用if条件语句判断,直接使用`return`返回`Bool`表达式
    return first_two_letter(s) and check_len(s) and check_number_position(s) and check_punctuation(s)


def first_two_letter(s):
    # 当需要返回Bool值时,不需要使用if条件语句判断,直接使用`return`返回`Bool`表达式
    return s[:2].isalpha()


def check_len(s):
    # 当需要返回Bool值时,不需要使用if条件语句判断,直接使用`return`返回`Bool`表达式
    return 2 <= len(s) <= 6


def check_number_position(s):
    num_positions = [i for i, char in enumerate(s) if char.isdigit()]
    # 简化判断条件,万物皆可作为判断条件Bool值
    if num_positions:
        first_num_pos = num_positions[0]
        last_num_pos = num_positions[-1]
        # 不需要区分数字的个数
        if s[first_num_pos] == "0" or (last_num_pos != len(s) - 1) or not is_numbers_connected(num_positions):
            return False
    return True


def is_numbers_connected(num_positions):
    # 这里我觉得很精髓的地方是`range(1, len(num_positions))`,因为是相邻两个数相比,所以最后一个数没办法和后一个比较,从`1`开始索引
    # 如果字符串中只有一个数字,那么`range(1, len(num_positions))`是空列表
    return all(num_positions[i] - num_positions[i - 1] == 1 for i in range(1, len(num_positions)))


def check_punctuation(s):
    return not any(char in ",." for char in s)


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("Invalid")


if __name__ == '__main__':
    main()
