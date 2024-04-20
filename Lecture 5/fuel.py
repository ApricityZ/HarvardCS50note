def convert(prompt):
    """
    Prompt the user to input a fraction, convert it to a percentage,
    and return the result.
    """
    fraction_input = prompt
    numerator, denominator = map(int, fraction_input.strip().split("/"))
    if denominator == 0:
        raise ZeroDivisionError
    elif numerator > denominator:
        raise ValueError
    percentage = round(numerator / denominator * 100, 2)
    return percentage


def gauge(percentage):
    """
    Return a grade based on the percentage.
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    """
    Main function to prompt user for a fraction, calculate its percentage,
    and output the corresponding grade.
    """
    while True:
        try:
            fraction_input = input("Enter a fraction (e.g., 3/4): ")
            fraction_percentage = convert(fraction_input)
            grade = gauge(fraction_percentage)
            print(f"Grade: {grade}")
        except ValueError:
            print("Invalid input. Please enter a valid fraction.")
        except ZeroDivisionError:
            print("Denominator cannot be zero.")


if __name__ == '__main__':
    main()

