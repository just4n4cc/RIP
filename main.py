# используется для сортировки
from operator import itemgetter

# Книга и библиотека
class Book:
    """Книга"""
    def __init__(self, id, title, author, pub_year, lib_id):
        self.id = id
        self.author = author
        self.title = title
        self.pub_year = pub_year
        self.lib_id= lib_id

class Library:
    """Библиотека"""
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

class BookLib:
    """
      'Книги библиотеки' для реализации
      связи многие-ко-многим
    """
    def __init__(self, lib_id, book_id):
        self.lib_id = lib_id
        self.book_id = book_id

# Книги
books = [
    Book(1, 'Преступление и наказание', 'Федор Достоевский', 1866, 1),
    Book(2, 'Война и мир', 'Лев Толстой', 1865, 1),
    Book(3, 'Старик и море', 'Эрнест Хемингуей', 1952, 1),
    Book(4, 'Превращение', 'Франц Кафка', 1915, 1),
    Book(5, 'Циники', 'Анатолий Мариенгоф', 1928, 2),
    Book(7, 'Числа', 'Виктор Пелевин', 2003, 2),
    Book(7, 'Хромая судьба', 'Аркадий и Борис Стругацкие', 1986, 2),
    Book(8, 'Наивно супер', 'Эрланд Лу', 1996, 3),
    Book(9, 'Чевенгур', 'Андрей Платонов', 1972, 3),
    Book(10, 'Горе от ума', 'Александр Грибоедов', 1825, 3),
]
# Библиотеки
libs = [
    Library(1, 'Библиотека Иностранной Литературы', '+7 (495) 915–36–41', 'spravka@libfl.ru'),
    Library(2, 'Российская Государственная Библиотека', '+7 (800) 100-57-90', 'nbros@rsl.ru'),
    Library(3, 'Библиотека им. Ф.М. Достоевского', '+7495 917 31 56', 'dostoevskylib@gmail.com'),
]

books_libs = [
    BookLib(1, 8),
    BookLib(1, 3),
    BookLib(1, 4),

    BookLib(2, 5),
    BookLib(2, 6),
    BookLib(2, 7),

    BookLib(3, 1),
    BookLib(3, 2),
    BookLib(3, 9),
    BookLib(3, 10),
]

def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [
        (b.title, b.author, l.name)
        for b in books
        for l in libs
        if b.lib_id == l.id
    ]
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, bl.lib_id, bl.book_id)
                         for l in libs
                         for bl in books_libs
                         if l.id == bl.lib_id]

    many_to_many = [(b.title, b.author, lib_name)
                    for lib_name, lib_id, book_id in many_to_many_temp
                    for b in books if b.id == book_id]

    print('Задание Б1')
    res1 = sorted(one_to_many, key=itemgetter(1))  # Сортировка по названиям
    print(res1)

    print('\nЗадание Б2')  # Список библиотек с количеством книг в каждой библиотеке
    res2 = []
    # Перебираем все библиотеки
    for l in libs:
        # Список библиотек
        l_books = list(filter(lambda i: i[2] == l.name, one_to_many))
        # Если библиотека не пустая
        if len(l_books) > 0:
            res2.append((l.name, len(l_books)))
        res2 = sorted(res2, key=lambda item: item[1], reverse=True)
    print(res2)

    print('\nЗадание Б3')  # Список авторов, у которых фамилия заканчивается на 'ов' и библиотеки
    res3 = {}
    for b in books:
        if str(b.author).endswith('ов'):
            l_books = list(filter(lambda i: i[1] == b.author, many_to_many))
            l_books_authors = [x for _, _, x in l_books]
            res3[b.author] = l_books_authors
    print(res3)


if __name__ == '__main__':
    main()
