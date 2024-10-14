# todo: База данных пользователя.
# Задан массив объектов пользователя


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

Написать фильтр, который будет выводить отсортированные объекты по возрасту (больше введенного),
первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
1. По возрасту
2. По первой букве
3. По группе

тип сортировки: 1

#Затем сообщение для ввода
Ввидите критерии поиска: 16

Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Запихиваем всё в функции

def search_by_age():
    user_age = int(input('Введите возраст пользователя: '))
    for i in range(len(users)):
        if users[i]['age'] > user_age:
            print(f"Пользователь: {users[i]['login']}, возраст: {users[i]['age']}, группа: {users[i]['group']}")
            print(users[i])

def search_by_name():
    user_name = input('Введите имя пользователя: ')
    for i in range(len(users)):
        if users[i]['login'][0] == user_name[0]:
            print(f"Пользователь: {users[i]['login']}, возраст: {users[i]['age']}, группа: {users[i]['group']}")
            print(users[i])

def search_by_group():
    user_group = input('Введите группу(guest, master, admin): ')
    for i in range(len(users)):
        if users[i]['group'] == user_group:
            print(f"Пользователь: {users[i]['login']}, возраст: {users[i]['age']}, группа: {users[i]['group']}")
            print(users[i])

# Вводим тип сортировки:

sorting_type = int(input('Как будем искать? 1 - по возрасту, 2 - по первой букве имени, 3 - по группе. Введите номер: '))

match sorting_type:
    case 1:  # По возрасту
        search_by_age()

    case 2:  # По первой букве
        search_by_name()

    case 3:  # По группе
        search_by_group()

