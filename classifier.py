import numpy as np
from sklearn import svm
from sklearn import cross_validation
from sklearn import metrics

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

def test(inFile):
  headers, data = read(inFile)

  vectors = np.array([[a[3],a[4],a[5],a[6],a[7],a[-1]] for a in data])
  results = []
  clf = svm.SVC(kernel='linear', C=0.04)

  for i in np.arange(100):
    np.random.shuffle(vectors) # randomize order, since similar tweets happen to be consequent (due to retweets and similar stuff)

    xTrain, xTest, yTrain, yTest = cross_validation.train_test_split(vectors.transpose()[:-1].transpose(), vectors.transpose()[-1], test_size=0.4)

    clf.fit(xTrain, yTrain)
    cvScores = cross_validation.cross_val_score(clf, xTrain, yTrain, cv=10, scoring='f1')
    testScore = clf.score(xTest, yTest)

    results.append((cvScores.mean(), testScore))

  for r in results:
    print("CV mean: %0.2f;  test score: %0.2f" % (r[0], r[1]))

if __name__ == '__main__':
  test('data.csv')