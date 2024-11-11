#todo: Числа в буквы
Замените числа, написанные через пробел, на буквы. Не числа не изменять.

Пример.
Input	                            Output
8 5 12 12 15	                    hello
8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!



# Решение

# Сгенерируем английский алфавит
from string import ascii_lowercase
alph = list(ascii_lowercase)
print(alph)

# По условию, 0 - это пробел, добавим его вручную
alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Создадим словарь, где ключом будет цифра, а значением - буква из алфавита.
dictionary = {k:v for k,v in enumerate(alphabet)}
print(dictionary)

# Разделим нашу числовую строку на элементы
line_numbers = '8 5 12 12 15 , 0 23 15 18 12 4 !'
line = [i for i in line_numbers.split()]
print(line)


# В этой строке, если элемент является числом (и если он есть в словаре), берём его значение из словаря.
# Если это не число, то оставляем, как есть.
list = [dictionary[int(i)] if i.isdigit() and int(i) in dictionary else i for i in line]
print(list)

# Объединяем все элементы воедино
final = ''.join(list)
print(final)
