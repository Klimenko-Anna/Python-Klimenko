class Clothes:
    """
    Базовый класс, который описывает модель одежды.
    """
    def __init__(self, size: int, material: str):
        """ Инициализация экземпляра класса. """
        self.size = size  # размер одежды
        self.material = material  # материал одежды

    def __str__(self):
        """ Метод возвращает строку, инициализирующую экземпляр. """
        return f"Это одежда размера {self.size} и из материала {self.material}"

    def __repr__(self):
        """ Метод возвращает валидную python строку, инициализирующую экземпляр. """
        return f"{self.__class__.__name__}(size={self.size}, material={self.material!r})"

    def is_clothes_fit(self, current_size: int) -> bool:
        """
        Метод проверяет, соответствует ли введённый размер размеру экземпляра одежды.
        Метод наследуется во всех дочерних классах,
        поскольку атрибут size также в них наследуется,
        а внутреннее устройство метода не меняется от класса к классу.
        """
        return current_size == self.size

    def season(self) -> str:
        """ Метод определяет, для какого сезона подходит одежда на основе её материала. """
        if self.material.lower() == "шерсть":
            return "Эта одежда подходит для зимы"
        elif self.material.lower() == "хлопок":
            return "Эта одежда подходит для лета"
        else:
            return "Эта одежда подходит как для лета, так и для зимы"


class Dress(Clothes):
    """ Дочерний класс одежды. Платье. """
    def __init__(self, size: int, material: str, length: int):
        """ Инициализация экземпляра класса. """
        super().__init__(size, material)  # вызов конструктора базового класса для его расширения
        self.length = length  # длина платья

    def __str__(self):
        """
        Метод возвращает строку, инициализирующую экземпляр.
        Используется перегрузка метода __str__ базового класса,
        поскольку теперь это не "одежда", а конкретно "платье",
        а также появился новый атрибут length.
        """
        return f"Это платье размера {self.size}, из материала {self.material} и длиной {self.length}"

    def __repr__(self):
        """
        Метод возвращает валидную python строку, инициализирующую экземпляр.
        Используется перегрузка метода __repr__ базового класса,
        поскольку появился новый атрибут length.
        """
        return f"{self.__class__.__name__}(size={self.size}, material={self.material!r}, length={self.length})"

    def season(self) -> str:
        """
        Метод определяет, для какого сезона подходит платье на основе его материала.
        Используется перегрузка метода season базового класса,
        поскольку теперь это не "одежда", а конкретно "платье"
        """
        if self.material.lower() == "шерсть":
            return "Это платье подходит для зимы"
        elif self.material.lower() == "хлопок":
            return "Это платье подходит для лета"
        else:
            return "Это платье подходит как для лета, так и для зимы"


if __name__ == "__main__":
    # Проведена проверка работоспособности методов
    dress = Dress(46, "хлопок", 56)
    print(dress)
    print(repr(dress))
    print(dress.season())
    print(dress.is_clothes_fit(48))
