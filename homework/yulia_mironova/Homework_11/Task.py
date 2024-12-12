class Book:
    material = 'бумага'
    is_text = True
    def __init__(self, title, author, pages, isbn, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved


class Textbook(Book):
    def __init__(self, title, author, pages, isbn, reserved, subject, group, istask):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.group = group
        self.istask = istask


book_1 = Book('Идиот', 'Достоевский', 500, '5-87818-228-9', False)
book_2 = Book('Война и мир', 'Толстой', 2000, '7-84828-323-2', False)
book_3 = Book('Незнайка', 'Носов', 100, '6-24227-225-9', False)
book_4 = Book('Мастер и Маргарита', 'Булгаков', 400, '5-82421-220-7', False)
book_5 = Book('Маленький принц', 'Сент-Экзюпери', 200, '4-25908-241-8', False)
textbook_1 = Textbook('Сборник задач', 'Макаров', 50, '2-15300-141-9', False,
                      'Математика', 7, False)
textbook_2 = Textbook('Атлас', 'Миров', 20, '3-25351-243-2', False,
                      'География', 10, False)
textbook_3 = Textbook('Прописи', 'Пушкарева', 40, '1-35400-841-2', False,
                      'Русский язык', 2, False)
book_1.reserved = True
book_5.reserved = True
textbook_3.reserved = True
print(f'Название: {book_1.title}, Автор: {book_1.author}, страниц: {book_1.pages}, материал: {book_1.material}'
      f'{', зарезервирована' if book_1.reserved else ''}')
print(f'Название: {book_2.title}, Автор: {book_2.author}, страниц: {book_2.pages}, материал: {book_2.material}'
      f'{', зарезервирована' if book_2.reserved else ''}')
print(f'Название: {book_3.title}, Автор: {book_3.author}, страниц: {book_3.pages}, материал: {book_3.material}'
      f'{', зарезервирована' if book_3.reserved else ''}')
print(f'Название: {book_4.title}, Автор: {book_4.author}, страниц: {book_4.pages}, материал: {book_4.material}'
      f'{', зарезервирована' if book_4.reserved else ''}')
print(f'Название: {book_5.title}, Автор: {book_5.author}, страниц: {book_5.pages}, материал: {book_5.material}'
      f'{', зарезервирована' if book_5.reserved else ''}')
print()
print(f'Название: {textbook_1.title}, Автор: {textbook_1.author}, страниц: {textbook_1.pages}, '
      f'предмет: {textbook_1.subject}, класс {textbook_1.group}{', зарезервирована' if textbook_1.reserved else ''}')
print(f'Название: {textbook_2.title}, Автор: {textbook_2.author}, страниц: {textbook_2.pages}, '
      f'предмет: {textbook_2.subject}, класс {textbook_2.group}{', зарезервирована' if textbook_2.reserved else ''}')
print(f'Название: {textbook_3.title}, Автор: {textbook_3.author}, страниц: {textbook_3.pages}, '
      f'предмет: {textbook_3.subject}, класс {textbook_3.group}{', зарезервирована' if textbook_3.reserved else ''}')
