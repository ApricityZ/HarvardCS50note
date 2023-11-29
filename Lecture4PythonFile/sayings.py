def main():
    hello("helloo")
    goodbye("world")


def hello(name):
    """

    :param name:
    """
    print(f"hello, {name}")


def goodbye(name):
    print(f"hello, {name}")


if __name__ == '__main__':  # 注意 "__name__"的使用
    main()
