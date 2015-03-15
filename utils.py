__author__ = 'vdziubak'

from numpy import float, e, log
import re


def reputation_score(total, relevant):
    return log(total + 1) * (2 * relevant - total) / total

def vectorize(raw_data):
    data = []

    for row in raw_data:
        # text = ' '.join([row[0], row[1]])
        text = row[1]
        if len(text.split(' ')) < 3:
            text = "#### " + row[0]
        # text = re.sub('http[s]?://(\S+)', '', text)  # remove urls
        # text = re.sub('i\s+liked\s+a\s+(video(\s+from)?|playlist)\s+|I\s+added\s+a\s+video\s+to\s+a\s+playlist\s+', '', text, flags=re.IGNORECASE)
        data.append(text)

    return data

def distance(vec1, vec2):
    pass