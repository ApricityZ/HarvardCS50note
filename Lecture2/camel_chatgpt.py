def camel2snake(camel_case):
    return "".join(["_" + char.lower() if char.isupper() else char for char in camel_case]).lstrip("_")


def main():
    camel_case = input("camelCase: ")
    snake_case = camel2snake(camel_case)
    print(snake_case)


if __name__ == '__main__':
    main()