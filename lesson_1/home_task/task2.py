# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"

age = '23'
foo = '23abc'
age = int(age)
foo = int(foo) # ValueError: invalid literal for int() with base 10: '23abc'
#foo невозможно преобразовать в число, потому что это значение переменной содержит буквы (нечисловые значения)?


# Преобразуйте переменную age в Boolean
# age = "123abc"

age = '123abc'
age = bool(age)

# Преобразуйте переменную flag в Boolean
# flag = 1

flag = 1
flag = bool(flag)


# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""

str_one = 'Privet'
str_two = ''
str_one = bool(str_one)
str_two = bool(str_two)

# Преобразуйте значение 0 и 1 в Boolean

x = bool(0)
y = bool(1)

# Преобразуйте False в строку

x = False
x = str(x)