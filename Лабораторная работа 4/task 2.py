# TODO импортировать необходимые модули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_file:  # TODO считать содержимое csv файла
        list_ = [line_ for line_ in csv.DictReader(input_file)]

    with open(OUTPUT_FILENAME, "w") as output_file:  # TODO Сериализовать в файл с отступами равными 4
        return json.dump(list_, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
