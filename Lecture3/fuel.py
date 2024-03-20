def get_fraction(prompt):
    while True:
        frac = input(prompt)
        chars = split_char(frac)
        try:
            x = int(chars[0])
            y = int(chars[1])
            if x > y:
                pass
            else:
                return round(x/y, 2) * 100
        except(ValueError, ZeroDivisionError):
            pass


def split_char(s: str):
    chars = s.strip().split("/")
    return chars

def output_result(frac):
    if frac <= 1:
        return "E"
    elif frac >= 99:
        return "F"
    else:
        return f"{int(frac)}%"
def main():
    frac = get_fraction("Fraction:")
    print(output_result(frac))


if __name__ == '__main__':
    main()

