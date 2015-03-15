#!/usr/bin/python3

import numpy as np
from sklearn import svm
from sklearn import cross_validation
from sklearn import metrics

from data_read import read_csv
from utils import reputation_score


def vectorize(data):
    vectors = np.array([[reputation_score(a[4], a[5]),  # 0 - reputation of author
                         reputation_score(a[6], a[7]),  # 1 - reputation of host
                         # reputation_score(a[8], a[9]),  # 2 - reputation of source
                         # a[10],                         # 3 - number of hashtags
                         # np.float(a[3]/a[2]),           # 4 - proportion of hashtags in a tweet
                         # a[11] ,                        # 5 - number of user mentions
                         a[-1]] for a in data])  # 6 - class

    return vectors


def test(data_src, c=0.04):
    headers, data = read_csv(data_src)
    # data:
    # 0  - Tweet text,
    # 1  - Link Title,
    # 2  - Tweet total length,
    # 3  - Hashtags length,
    # 4  - Author total tweets,
    # 5  - Author quality tweets,
    # 6  - Host total urls,
    # 7  - Host quality urls,
    # 8  - Source total urls,
    # 9  - Source quality urls,
    # 10 - Number of hashtags,
    # 11 - Number of user mentions,
    # 12 - Class
    vectors = vectorize(data)

    results = []
    clf = svm.SVC(kernel='linear', C=c)

    for i in np.arange(100):
        np.random.shuffle(vectors)  # randomize order

        x_train, x_test, y_train, y_test = cross_validation.train_test_split(vectors.T[:-1].T, vectors.T[-1],
                                                                             test_size=0.4)

        clf.fit(x_train, y_train)
        cv_scores = cross_validation.cross_val_score(clf, x_train, y_train, cv=10, scoring='accuracy')
        test_score = clf.score(x_test, y_test)

        results.append((cv_scores.mean(), test_score))

    for r in results:
        print("CV mean: %0.2f;  test score: %0.2f" % (r[0], r[1]))

    # return clf


if __name__ == '__main__':
    test('data.csv')