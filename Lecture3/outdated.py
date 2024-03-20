def check_input():
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    time_input = input("Data: ").strip()
    if "/" in time_input:
        month, day, year = time_input.split("/")
        # if not all(int(item).isdigit() for item in time_input.split("/")):
            # return False
        if month[0].isalpha():
            return False
        if not 1 <= int(month) <= 12:
            return False
        elif not 1 <= int(day) <= 31:
            return False
        else:
            return f"{year}-{int(month):02}-{int(day):02}"
    elif "," in time_input:
        times = time_input.split()
        month, day, year = [char.strip(",") for char in times]
        if month not in month_list:
            return False
        elif int(day) not in range(1,32):
            return False
        else:
            return f"{int(year)}-{month_list.index(month)+1:02}-{int(day):02}"
    else:
        return False

def outdate(s):
    print(s)
def main():
    while True:
        time = check_input()
        if time:
            print(time)
            break
        else:
            check_input()

if __name__ == '__main__':
    main()
