from pyfiglet import Figlet

figlet = Figlet()
import sys
import random


def output_front(str_input, front):
    # front = Figlet.getFonts()
    # random_front = random.choice(front)
    # front = front
    figlet.setFont(font=front)
    print(figlet.renderText(str_input))


def parse_argv( argvs):
    font = figlet.getFonts()
    if len(argvs) == 1:
        str_input = input().strip()
        font = random.choice(font)
        output_front(str_input,font)
    elif len(argvs) == 3:
        if argvs[1] == "-f" or argvs[1] == "--font" and argvs[2] in font:
            str_input = input().strip()
            output_front(str_input, argvs[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


def main():
    parse_argv(sys.argv)

if __name__ == '__main__':
    main()
