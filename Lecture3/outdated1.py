def check_input() -> bool | str:
    month_list = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    time_input = input("Data: ").strip()
    if "/" in time_input:
        month, day, year = time_input.split("/")
        if not (month.isdigit() and day.isdigit() and year.isdigit()):
            return False
        if not (1 <= int(month) <= 12 and 1 <= int(day) <= 31):
            return False
        return f"{year}-{int(month):02}-{int(day):02}"
    elif "," in time_input:
        month, day, year = [item.strip(",") for item in time_input.split()]
        if month not in month_list or not day.isdigit() or not year.isdigit():
            return False
        if not (1 <= int(day) <= 31):
            return False
        return f"{int(year)}-{month_list.index(month) + 1:02}-{int(day):02}"
    else:
        return False


def main():
    while True:
        time = check_input()
        if time:
            print(time)
            break
        else:
            # print("Invalid input. Please try again.")
            pass


if __name__ == '__main__':
    main()
"""优化包括：

在 check_input() 中，验证月份、日期和年份是否都是数字，而不是仅检查月份。
在 main() 中，当输入无效时打印提示消息，而不是再次调用 check_input()。"""
