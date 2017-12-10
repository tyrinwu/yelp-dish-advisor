import numpy as np
from annoy import AnnoyIndex


def test():
    t = AnnoyIndex(500)
    v = 1 * (np.random.rand(500) > 0.95)
    t.load("test_huge_vec.ann")
    result = t.get_nns_by_vector(v, 10)
    print(result)

test()

