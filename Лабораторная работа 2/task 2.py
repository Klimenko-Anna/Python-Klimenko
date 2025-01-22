from typing import Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """
    Класс описывает модель книги
    """

    def __init__(self, id_: int, name: str, pages: int):
        """ Инициализация экземпляра класса """
        self.id_ = id_  # идентификатор книги
        self.name = name  # название книги
        self.pages = pages  # количество страниц в книге

    def __str__(self) -> str:
        """ Метод возвращает строку, инициализирующую экземпляр """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """ Метод возвращает валидную python строку, инициализирующую экземпляр """
        return f"{self.__class__.__name__}(id_={self.id_}, name={self.name!r}, pages={self.pages})"


class Library:
    """
    Класс описывает модель библиотеки
    """

    def __init__(self, books: Optional[list[Book]] = []):
        """ Инициализация экземпляра класса """
        self.books = books  # список книг

    def get_next_book_id(self) -> int:
        """ Метод возвращает идентификатор для добавления новой книги в библиотеку """
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1  # идентификатор последней книги

    def get_index_by_book_id(self, book_id: int) -> int:
        """ Метод возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса """
        for id_name, book in enumerate(self.books):
            if book.id_ == book_id:
                return id_name
            else:
                raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
