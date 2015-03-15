__author__ = 'vdziubak'

from numpy import float


def read_csv(csv_file):
    data = []

    with open(csv_file) as f:
        headers = f.readline().strip().split(',')

        for row in f.readlines():
            row = row.strip().split(',')

            for index, item in enumerate(row):
                try:
                    row[index] = float(item)
                except ValueError:
                    pass

            data.append(row)

    return headers, data