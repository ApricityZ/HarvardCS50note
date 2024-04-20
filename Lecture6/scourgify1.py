import sys
import csv
from typing import Tuple


def parse_argv(argvs: list[str]) -> Tuple[str, str]:
    if len(argvs) != 3:
        raise ValueError("Usage: python script.py <input_file.csv> <output_file.csv>")

    input_file = argvs[1]
    output_file = argvs[2]

    if not (input_file.endswith('.csv') and output_file.endswith('.csv')):
        raise ValueError("Both files must have a .csv extension")

    return input_file, output_file


def write_to_csv(files: Tuple[str, str]):
    input_file, output_file = files

    try:
        with open(input_file) as infile:
            reader = csv.DictReader(infile)
            data = []
            for row in reader:
                first_name, last_name = row["name"].strip("\"").split(",")
                data.append({"first": first_name.strip(), "last": last_name.strip(), "house": row["house"]})

            fieldnames = ["first", "last", "house"]
            with open(output_file, "w", newline="") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                for info in data:
                    writer.writerow(info)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not read {input_file}")


def main():
    try:
        write_to_csv(parse_argv(sys.argv))
    except (ValueError, FileNotFoundError) as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
