__author__ = 'vdziubak'

import re

def vectorize(raw_data):
    data = []

    for row in raw_data:
        text = ' '.join([row[0], row[1]])
        text = re.sub('http[s]?://(\S+)|[#@](\S+)', '', text)  # remove urls, hashtags, user mentions
        data.append(text)

    return data

class Cluster:
    def __init__(self, vector):
        self.centroid = vector
        self.vectors = [vector]

    def add(self, vector):
        self.vectors.append(vector)
        self.recalculateCentriod()

    def 

def cluster(vector):
