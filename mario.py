def main():
    height = int(input(("Height:")))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print(i, end=",")
        print("#" * i)


if __name__ == "__main__":
    main()


"""
调试代码：
    设置断点
    步进：一行一行代码开始执行
    步过：不深入运行当前行，只是正常运行当前行
    步出：从步入的方法内执行完该方法，然后退出到方法调用处。
"""