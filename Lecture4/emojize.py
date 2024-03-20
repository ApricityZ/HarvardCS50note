import emoji
def main():
    sentence = input("Input: ").strip()
    convert_sentence = emoji.emojize(sentence)
    print(convert_sentence)

if __name__ == '__main__':
    main()