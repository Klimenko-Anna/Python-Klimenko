import doctest
from typing import Union


"Первый класс - Размер комнаты"


class Room:
    def __init__(self, length: Union[int, float], width: Union[int, float]):
        """
Создание и подготовка к работе объекта "Комната"

:param length: Длина стены комнаты
:param width: Ширина стены комнаты

Пример:
>>> room = Room(145, 259)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина стены должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина стены должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стены должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина стены должна быть положительным числом")
        self.width = width

    def area(self) -> (int, float):
        """
Функция, которая рассчитывает площадь комнаты

:return: Площадь комнаты по формуле: self.length * self.width
    
Пример:
>>> room = Room(145, 259)
>>> room.area()
        """
        ...

    def perimetr(self) -> (int, float):
        """
Функция, которая рассчитывает периметр комнаты

:return: Периметр комнаты по формуле: (self.length + self.width) * 2

Пример:
>>> room = Room(145, 259)
>>> room.perimetr()
        """
        ...


"Второй класс - Игровой прогресс"


class GameProgress:
    def __init__(self, game: str, level: int):
        """
Создание и подготовка к работе объекта "Прогресс"

:param game: Название игры
:param level: Уровень в игре

Пример:
>>> progress = GameProgress("Mario", 259)  # инициализация экземпляра класса
        """
        if not isinstance(game, str):
            raise TypeError("Название игры должно быть типа str")
        self.game = game

        if not isinstance(level, int):
            raise TypeError("Уровень в игре должен быть типа int")
        if level < 0:
            raise ValueError("Уровень в игре не может быть отрицательным числом")
        self.level = level

    def is_start_level(self) -> bool:
        """
Функция, которая проверяет, находится ли игрок в начале игры

:return: Является ли уровень начальным

Пример:
>>> progress = GameProgress("Mario", 0)
>>> progress.is_start_level()
        """
        ...

    def next_level(self, new_level: int) -> None:
        """
Функция, которая увеличивает прогресс в игре на количество пройденных уровней
следующим образом после выполнения всех проверок:
self.level += new_level

:param new_level: Количество новых пройденных уровней

Пример:
>>> progress = GameProgress("Mario", 269)
>>> progress.next_level(2)
        """
        if not isinstance(new_level, int):
            raise TypeError("Количество новых пройденных уровней должно быть типа int")
        if new_level < 0:
            raise ValueError("Количество новых пройденных уровней должно быть положительным числом")
        ...


"Третий класс - Итоговая успеваемость"


class Grade:
    def __init__(self, subject: str, score: int):
        """
Создание и подготовка к работе объекта "Успеваемость"
Предполагается, что это итоговый срез за семестр или год

:param subject: Название дисциплины
:param score: Оценка

Пример:
>>> grade = Grade("Алгебра", 5)  # инициализация экземпляра класса
        """
        if not isinstance(subject, str):
            raise TypeError("Название дисциплины должно быть типа str")
        self.subject = subject

        if not isinstance(score, int):
            raise TypeError("Оценка должна быть типа int")
        if score < 0:
            raise ValueError("Оценка должна быть положительным числом")
        if score > 5:
            raise ValueError("Оценка должна быть не больше 5")
        self.score = score

    def is_excellent(self) -> bool:
        """
Функция, которая проверяет, является ли студент отличником по предмету

:return: Является ли студент отличником

Пример:
>>> grade = Grade("Алгебра", 5)
>>> grade.is_excellent()
        """
        ...

    def is_good(self) -> bool:
        """
Функция, которая проверяет, является ли студент хорошистом по предмету

:return: Является ли студент хорошистом

Пример:
>>> grade = Grade("Русский язык", 4)
>>> grade.is_good()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
