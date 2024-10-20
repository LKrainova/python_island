# todo: Шифр Цезаря
Описание шифра.
В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
является одним из самых простых и широко известных методов шифрования.
Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

Задача.
Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.


alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
cezary = open('message.txt', 'r+', encoding='utf-8')

# Шифруем строку 1 (символы сдвигаются влево на 1)

l_1 = cezary.readline().lower()
line_1 = list(l_1)
for i in range(len(line_1)):
    if line_1[i] in alphabet:
        index = alphabet.index(line_1[i])
        line_1[i] = alphabet[index - 1]
print(l_1)
joined_line_1 = ''.join(line_1)
print(joined_line_1)


# Шифруем строку 2 (символы сдвигаются влево на 2)

l_2 = cezary.readline().lower()
line_2 = list(l_2)
for i in range(len(line_2)):
    if line_2[i] in alphabet:
        index = alphabet.index(line_2[i])
        line_2[i] = alphabet[index - 2]
print(l_2)
joined_line_2 = ''.join(line_2)
print(joined_line_2)


# Шифруем строку 3 (символы сдвигаются влево на 3)

l_3 = cezary.readline().lower()
line_3 = list(l_3)
for i in range(len(line_3)):
    if line_3[i] in alphabet:
        index = alphabet.index(line_3[i])
        line_3[i] = alphabet[index - 3]
print(l_3)
joined_line_3= ''.join(line_3)
print(joined_line_3)


# Шифруем строку 4 (символы сдвигаются влево на 4)

l_4 = cezary.readline().lower()
line_4 = list(l_4)
for i in range(len(line_4)):
    if line_4[i] in alphabet:
        index = alphabet.index(line_4[i])
        line_4[i] = alphabet[index - 4]
print(l_4)
joined_line_4= ''.join(line_4)
print(joined_line_4)


# Шифруем строку 5 (символы сдвигаются влево на 5)

l_5 = cezary.readline().lower()
line_5 = list(l_5)
for i in range(len(line_5)):
    if line_5[i] in alphabet:
        index = alphabet.index(line_5[i])
        line_5[i] = alphabet[index - 5]
print(l_5)
joined_line_5= ''.join(line_5)
print(joined_line_5)
cezary.close()


