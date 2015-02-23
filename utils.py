__author__ = 'vdziubak'

from numpy import float, e, log


def reputation_score(total, relevant):
    return log(total + 1) * (2 * relevant - total) / total
