from copy import deepcopy
from numpy import array


class Cluster:
    def __init__(self):
        self._dim = None
        self._vectors = []
        self._centroid = []

    @property
    def dim(self):
        return self._dim
    @dim.setter
    def dim(self, value):
        self._dim = value

    @property
    def centroid(self):
        return self._centroid

    @property
    def vectors(self):
        return self._vectors

    def add(self, vector):
        if not self.dim:
            self.dim = len(vector)
        elif len(vector) != self.dim:
            raise ValueError("trying to add vectors with wrong dimension")

        self.dim = len(vector)
        self.vectors.append(deepcopy(vector))
        self._update_centroid()

    def _update_centroid(self):
        self._centroid = [col.mean() for col in array(self.vectors).T]