import sys
from PIL import Image, ImageOps

def parse_argv(argvs: list[str]) -> tuple[str, str]:
    if len(argvs) != 3:
        # print(11111)
        raise ValueError("Usage error")

    input_file = argvs[1]
    output_file = argvs[2]

    exten = [arg.split(".")[1].lower() for arg in argvs[1:]]
    exten = set(exten)
    if len(exten)!=1 or not exten < {"jpg","jpeg"}:
        raise ValueError("File type error")

    return input_file, output_file


def p_shit(photos):
    bphoto, aphoto = photos
    shirt = Image.open("shirt.png")
    size = shirt.size
    try:
        bp = Image.open(bphoto)
        bp = ImageOps.fit(bp,size)
        bp.paste(shirt,shirt)
        bp.save(aphoto)
    except FileNotFoundError:
        raise ValueError("File Not exist")


def main():
    try:
        p_shit(parse_argv(sys.argv))
    except (ValueError) as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
