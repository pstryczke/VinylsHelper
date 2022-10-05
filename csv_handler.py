import csv
from typing import List, Iterable


def save_csv(file: str, data: List[list]):
    with open(file, 'w', encoding="utf8", newline='') as stream:
        writer = csv.writer(stream, delimiter=';')
        for row in data:

            writer.writerow(row)


def load_csv(file: str) -> Iterable:
    with open(file, 'r', encoding="utf8") as stream:
        return csv.reader(stream, delimiter=';')
