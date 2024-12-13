class Book:
    material = 'бумага'
    is_text = True
    def __init__(self, title, author, pages, isbn, reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def print_book(self):
        print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, материал: {self.material}"
              f"{', зарезервирована' if self.reserved else ''}")


class Textbook(Book):
    def __init__(self, title, author, pages, isbn, reserved, subject, group, istask):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.group = group
        self.istask = istask

    def print_testbook(self):
        print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, "
              f"предмет: {self.subject}, класс {self.group}{', зарезервирована' if self.reserved else ''}")


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
book_1.print_book()
book_2.print_book()
book_3.print_book()
book_4.print_book()
book_5.print_book()
print()
textbook_1.print_testbook()
textbook_2.print_testbook()
textbook_3.print_testbook()
