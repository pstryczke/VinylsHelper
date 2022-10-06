import csv
from typing import List


def save_csv(file: str, data: List[list]):
    with open(file, 'w', encoding="utf8", newline='') as stream:
        writer = csv.writer(stream, delimiter=';')
        for row in data:
            writer.writerow(row)


def load_csv(file: str) -> List:
    with open(file, 'r', encoding="utf8") as stream:
        output = list()
        for row in csv.reader(stream, delimiter=';'):
            output.append(row)
        return output
