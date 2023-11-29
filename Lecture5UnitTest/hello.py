def main():
    name = input("What's your name?")
    output = hello(name)
    print(output)


def hello(to="world"):
    # print("hello,", to)   # 此时没有返回值无法测试
    return f"hello, {to}"


if __name__ == '__main__':
    main()