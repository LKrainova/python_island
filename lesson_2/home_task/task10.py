# # todo: 10.1 Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# # todo: 10.2 Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
# # Примечание: В задании  требуется вывести логическое значение True, если выражение
# # для введеных исходных данных является истинным, и значение False в противном случае.


a = int(input('Введите целое число А, и мы проверим, является ли оно чётным!'))
if a % 2 == 0:
    print(True)
else:
    print(False)

b = int(input('Введите целое число В, и мы проверим, является ли оно нечётным!'))
if b % 2 != 0:
    print(True)
else:
    print(False)

