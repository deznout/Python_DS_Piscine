import sys


def caesar_cipher(command, text, shift):
    shift = int(shift)
    dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for i in text:
        if i in cyrillic:
            return print("Doesn't work with cyrillic")
    if command == "decode":
        translated = ''
        text = text.upper()
        for symbol in text:
            if symbol in dictionary_upper:
                num = dictionary_upper.find(symbol)
                num = num - shift
                if num < 0:
                    num = num + len(dictionary_upper)
                translated = translated + dictionary_upper[num]
            else:
                translated = translated + symbol
        print(translated)
    elif command == "encode":
        res, n = [], ""
        for i in range(len(text)):
            if text[i] in dictionary:
                n = dictionary
            elif text[i] in dictionary_upper:
                n = dictionary_upper
            else:
                res.append(text[i])
            if text[i] in n:
                for j in range(len(n)):
                    if 0 <= j + shift < len(n) and text[i] == n[j]:
                        res.append(n[j + shift])
                    elif j + shift >= len(n) and text[i] == n[j]:
                        res.append(n[(1 - j - shift) % (len(n) - 1)])
                    elif j + shift < 0 and text[i] == n[j]:
                        res.append(n[(j + shift) % len(n)])
        print(''.join(res))
    else:
        print("Wrong command")


if __name__ == '__main__':
    if len(sys.argv) == 4:
        caesar_cipher(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Please, put four arguments")
