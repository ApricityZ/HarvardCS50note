import sys
from sys import argv
from tabulate import tabulate
import csv

def parse_argv(argvs: str) -> str:
    if len(argvs) == 2:
        if "csv" in argvs[1].strip().split("."):
            return argvs[1]
        else:
            print("Not a CSV file")
            sys.exit(1)
    elif len(argvs) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        print("Too many command-line arguments")
        sys.exit(1)


def format_trans(file_csv):
    menu = []
    try:
        with open(file_csv) as file:
            reader = csv.reader(file)
            header = next(reader)
            header = list(header)
            # print(header)
            for line in reader:
                # menu.append({"Sicilian Pizza": line[0], "Small": line[1], "Large": line[2]})
                # menu.append({header[0]:line[0], header[1]:line[1], header[2]:line[2]})
                menu.append([line[0], line[1],line[2]])
            print(tabulate(menu, headers=header, tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


def main():
    format_trans(parse_argv(argv))


if __name__ == '__main__':
    main()