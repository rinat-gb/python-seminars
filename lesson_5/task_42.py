#!/usr/bin/python
#
# 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#
def rle_encode(text):
    out_string = ""
    i = 0
    while (i < len(text)):
        count = 1
        ch = text[i]
        j = i
        while (j < len(text)-1):
            if (text[j] == text[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        out_string = out_string + str(count) + ch
        i = j + 1
    return out_string


def rle_decode(text):
    out_string = ""
    i = 0
    j = 0
    while (i < len(text)):
        count = int(text[i])
        ch = text[i + 1]
        for j in range(count):
            out_string = out_string+ch
            j = j + 1
        i = i + 2
    return out_string

in_text = input(f'Введите строку для сжатия: ')
encoded_string = rle_encode(in_text)
print(f'Сжатая строка: "{encoded_string}"')
decoded_string = rle_decode(encoded_string)
print(f'Восстановленная строка: "{decoded_string}"')
