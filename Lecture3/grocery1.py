def shopping_list():
    lst = []
    while True:
        try:
            item = input().strip().lower()
            if not item:
                break
            lst.append(item)
        except EOFError:
            break
    return lst


def output_list(lst):
    count_dict = {}
    """count_dict[item] = count_dict.get(item, 0) + 1：这行代码实现了计数的逻辑。首先，count_dict.get(item, 0) 
    会尝试从 count_dict 字典中获取键为 item 的值。如果该键存在，则返回对应的值，如果不存在，则返回默认值 0。然后，我们将这个值加 1，
    以统计当前物品在列表中出现的次数。最后，将结果存储回 count_dict[item] 中，以更新物品的计数。"""
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1

    for item, count in sorted(count_dict.items()):
        print(f"{count} {item.upper()}")


def main():
    grocery_list = shopping_list()
    output_list(grocery_list)


if __name__ == '__main__':
    main()
