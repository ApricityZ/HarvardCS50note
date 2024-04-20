def shorten(sentence:str) ->str:
    # vowels = ["A", "E", "I", "O", "U"]
    # vowels += [c.lower() for c in vowels]
    # 使用字符串"AEIOUaeiou"来代替列表储存元音字符,这样做可以更加高些简洁
    # 字符串是一个iterable对象
    vowels = "AEIOUaeiou"
    return "".join(["" if char in vowels else char for char in sentence])


def main():
    sentence = input("Input: ")
    omitted_sentence = shorten(sentence)
    print(omitted_sentence)


if __name__ == '__main__':
    main()