def shopping_list():
    _list = []
    while True:
        try:
            _list.append(input().strip().lower())
        except EOFError:
            return _list


def output_list(l: list):
    processed = set()
    # dict = {index:item  for index, item in enumerate(l)}
    count_dict = {item: l.count(item) for item in l}
    sorted_set = sorted(set(l))
    # print(index, item, sep=" ")
    for i in sorted_set:
        if i not in processed:
            print(count_dict[i], i.upper(), sep=" ")
            processed.add(i)  # 不是append


def main():
    grocery_list = shopping_list()
    output_list(grocery_list)


if __name__ == '__main__':
    main()
