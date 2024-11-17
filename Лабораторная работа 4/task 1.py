# TODO решите задачу
import json


FILE_NAME = 'input.json'


def task() -> float:
    with open(FILE_NAME) as f:
        file = json.load(f)

    total = sum([item["score"] * item["weight"] for item in file])
    return round(total, 3)


print(task())
