import sys

def count_lines(file):
    count = 0
    c_all = 0
    for line in file:
        c_all += 1
        if line.lstrip().startswith("#") or line.strip() == "":
            count += 1
    return c_all-count

def main():
    if len(sys.argv) == 2:
        if "py" in sys.argv[1].split("."):
            try:
                with open(sys.argv[1]) as file:
                    lines = count_lines(file)
                    print(lines)
            except FileNotFoundError:
                print("File does not exist")
                sys.exit(1)
        else:
            print("Not a Python file")
            sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line argument")
        sys.exit(1)
    else:
        print("Too many command-line argument")
        sys.exit(1)

if __name__ == '__main__':
    main()