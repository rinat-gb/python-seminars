#!/usr/bin/python
#
# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#
text = input("Введите текстовую строку: ")
out_list = []
for word in text.split(' '):
    if 'а' not in word and 'б' not in word and 'в' not in word:
        out_list.append(word)
print(f'Из текста "{text}" удалены все слова, в которых были буквы ''а'', ''б'' или ''в'':')
print('"', ' '.join(out_list), '"', sep='')
