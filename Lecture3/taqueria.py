def order():
    menu_dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    orders = []
    while True:
        # order = input("Item: ")
        try:
            order = input("Item: ").title()
            # order_checked = [order.title() if order.title() in menu_dict else ""]
            if order in menu_dict:
                orders.append(order)
                print("${:.2f}".format(sum([menu_dict[per_order] for per_order in orders])))
            else:
                pass
        except EOFError:
            break


def main():
    order()


if __name__ == '__main__':
    main()