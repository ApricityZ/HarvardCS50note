def value(sentence):
    money = 0
    words0 = sentence.split()
    words = []
    for word in words0:
        words.extend(word.split(","))
    if sentence[0].lower() == "h":
        if words[0].lower() == "hello":
            money = 0
            return money
        else:
            money = 20
            return money
    else:
        money = 100
        return money


def main():
    sentence = input("Greeting:").strip()
    money = int(value(sentence))
    print(f"${money}")

if __name__ == '__main__':
    main()
