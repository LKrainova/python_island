todo: Заданы множества
все пользователи
all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
# пользователи не в сети
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}

Вычислить пользователей online

# Тут нужно посчитать разницу между множествами

all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}
online_users = all_users.difference(offline_users)
print(online_users)


#todo: Заданы множества
#Даны читатели книг
readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1' }

#Даны читатели газет
readers_magazines = { 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}

Найти пользователей кто читает и книги, и газеты


# Здесь надо найти пересечение множеств

readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1'}
readers_magazines = {'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
both_readers = readers_books.intersection(readers_magazines)
print(both_readers)


