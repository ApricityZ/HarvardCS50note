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
    return True if 2 <= len(s) <=6 else False

def check_nmuber_position(s):
    if any(char.isdigit() for char in s):
        num_position = [i for i,char in enumerate(s) if char.isdigit()]
        if s[num_position[0]] == 0:
            return False
        elif num_position[-1] == len(s):
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