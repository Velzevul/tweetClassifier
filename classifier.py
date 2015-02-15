import numpy as np

def read(inFile):
  data = []

  with open(inFile) as f:
    headers = f.readline().strip().split(',')

    for row in f.readlines():
      row = row.strip().split(',')

      for index, item in enumerate(row[3:]):
        print(row[index])
        row[index + 3] = np.float_(item)

      data.append(row)

  return headers, data