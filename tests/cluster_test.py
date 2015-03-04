from cluster import Cluster
import unittest

class ClusterTest(unittest.TestCase):
    def setUp(self):
        self.cluster = Cluster()

    def test_add_uniqueness(self):
        v = [1,2,3]
        self.cluster.add(v)
        v.append(4)
        self.assertEqual(self.cluster.vectors, [[1,2,3]])

    def test_add(self):
        v = [1,2,3]
        self.cluster.add(v)
        self.assertEqual(self.cluster.vectors, [v])
        self.assertEqual(self.cluster.centroid, v)

    def test_centroid(self):
        vecs = [[1,2,3], [4,5,6], [7,8,9]]
        center = [4,5,6]

        for vec in vecs:
            self.cluster.add(vec)

        self.assertEqual(self.cluster.centroid, center)

if __name__ == '__main__':
    unittest.main()