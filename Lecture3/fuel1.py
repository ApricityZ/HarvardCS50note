def get_fraction_percentage(prompt):
    """
    Prompt the user to input a fraction, convert it to a percentage,
    and return the result.
    """
    while True:
        fraction_input = input(prompt)
        numerator, denominator = split_fraction(fraction_input)  # 更简洁
        try:
            if numerator > denominator:
                pass
            else:
                return round(numerator / denominator, 2) * 100
        except (ValueError, ZeroDivisionError):
            pass


def split_fraction(fraction_string):
    """
    Split a string representing a fraction into its numerator and denominator.
    """
    numerator, denominator = fraction_string.strip().split("/")  # 在已知分割结果后,这样写更加的简洁
    return int(numerator), int(denominator)  # 将不同功能划分在不同的函数中,增强代码的复用性和简洁性


def output_result(percentage):
    """
    Return a grade based on the percentage.
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"


def main():
    """
    Main function to prompt user for a fraction, calculate its percentage,
    and output the corresponding grade.
    """
    fraction_percentage = get_fraction_percentage("Fraction: ")
    print(output_result(fraction_percentage))


if __name__ == '__main__':
    main()
