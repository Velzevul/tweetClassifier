__author__ = 'vdziubak'

from numpy import float, e, log
import re


def reputation_score(total, relevant):
    return log(total + 1) * (2 * relevant - total) / total

def vectorize(raw_data):
    data = []

    for row in raw_data:
        text = ' '.join([row[0], row[1]])
        text = re.sub('http[s]?://(\S+)|[#@](\S+)', '', text)  # remove urls, hashtags, user mentions
        data.append(text)

    return data

def distance(vec1, vec2):
    pass