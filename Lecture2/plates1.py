def is_valid(s):
    s = s.strip()
    if first_two_letter(s) and check_len(s) and check_nmuber_position(s) and check_punctuation(s):
        return True
    else:
        return False


def first_two_letter(s):
    s_slice = s[0:2]
    return True if s_slice.isalpha() else False


def check_len(s):
    return True if 2 <= len(s) <= 6 else False


def check_nmuber_position(s):
    if any(char.isdigit() for char in s):
        num_position = [i for i, char in enumerate(s) if char.isdigit()]
        if s[num_position[0]] == "0":
            return False
        elif len(num_position) == 1 and num_position[-1] == len(s) - 1:
            # elif s[num_position[-1]].isdigit():
            return True
        # 分类的话同时也需要检查最后一位是不是数字,否则`CS50A`会被判断为`Valid`
        elif len(num_position) > 1 and all(
                num_position[i] - num_position[i - 1] == 1 for i in range(1, len(num_position))) and num_position[
            -1] == len(s) - 1:
            return True
        else:
            return False
    else:
        return True


def check_punctuation(s):
    if any(char in ",. " for char in s):
        return False
    else:
        return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("Invalid")


if __name__ == '__main__':
    main()
