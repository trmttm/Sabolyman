import csv
from typing import Iterable


def execute(file_name: str, data: Iterable):
    with open(file_name, 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)
