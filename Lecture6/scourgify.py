import sys
from sys import argv
import csv
from typing import Tuple


def parse_argv(argvs: list[str]) -> tuple[str, str]:
    if len(argvs) == 3:
        if "csv" in argvs[1].strip().split(".") and "csv" in argvs[2].strip().split("."):
            return argvs[1],argvs[2]
        else:
            print("Not a CSV file")
            sys.exit(1)
    elif len(argvs) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        print("Too many command-line arguments")
        sys.exit(1)


def write_to_csv(name):
    before_file =name[0]
    after_file = name[1]

    info = []
    try:
        with open(before_file) as bfile:
            reader = csv.DictReader(bfile)
            # headers = next(reader)
            for row in reader:
                last_name, first_name = row["name"].strip("\"").split(",")

                info.append({"first":first_name.strip(), "last":last_name.strip(), "house":row["house"]})

            fieldnames = ["first", "last", "house"]
            with open(after_file, "w", newline="") as afile:
                writer = csv.DictWriter(afile, fieldnames=fieldnames)
                writer.writeheader()
                for inf in info:
                    writer.writerow(inf)
    except FileNotFoundError:
        sys.exit(f"Could not read {before_file}")

def main():
    write_to_csv(parse_argv(argv))
if __name__ == '__main__':
    main()
