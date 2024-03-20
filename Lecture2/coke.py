# def main():
#     amount_threshold = 50
#     amount_count = 0
#     while amount_count < amount_threshold:
#         insert_coin = int(input("Insert Coin:"))
#         if insert_coin in [25, 10, 5]:
#             amount_count += insert_coin
#             if amount_count < 50:
#                 print(f"Amount Due: {amount_threshold - amount_count}")
#         else:
#             break
#     print(f"Change Owed:{amount_count - amount_threshold}")
#
#
# if __name__ == '__main__':
#     main()
def main():
    amount_threshold = 50
    amount_count = 0
    while amount_count < amount_threshold:
        insert_coin = int(input("Insert Coin:"))
        if insert_coin in [25, 10, 5]:
            amount_count += insert_coin
            if amount_count < amount_threshold:
                print(f"Amount Due: {amount_threshold - amount_count}")
            else:
                print(f"Change Owed: {amount_count - amount_threshold}")
        else:
            print("Amount Due: 50")



if __name__ == '__main__':
    main()
