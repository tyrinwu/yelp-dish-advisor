"""The script use annoy (Approximate Nearest Neighhors Oh Yeah)
library. The purpose is to build a tree for searching based on
random projection.

Because it uses random projection, there could be cases that it separates
two close points into 2 far away planes.

TODO: Location based hashing and similarity based hashing

Dependency:
    annoy

Usage:
    Each time you update the source data, one needs to call this
    script to rebuild a tree. Once a tree is built, one cannot
    add new items. (limitation of the package)

Example:
    from annoy import AnnoyIndex
    import random

    f = 40
    t = AnnoyIndex(f)  # Length of features
    for i in range(1000):
        v = [random.gauss(0, 1) for z in range(f)]
        t.add_item(i, v) # i (index that must be an integer
                         # the vector corresponds to i

    t.build(10) # 10 trees. More trees means more precision.
    t.save('test.ann')
    ###################################
    u = AnnoyIndex(f)
    u.load('test.ann') # super fast, will just mmap the file
    print(u.get_nns_by_item(0, 1000)) # will find the 1000 nearest neighbors

Note:
    Users have to maintain a map if their indexes are integers.
"""
from annoy import AnnoyIndex


class AnnoyTreeBuilder(object):
    """Build a annoy tree and save it."""

    def __init__(self, num_tree=2):
        self.num_tree = num_tree

    def build_iter(self, file_name, generator, num_feat, num_input, func=None):
        tree = AnnoyIndex(num_feat)
        if func is None:
            func = lambda x: x
        try:
            for idx, val in enumerate(generator):
                if idx >= num_input:
                    break
                if self.contain_missing_data(val, num_feat):
                    continue
                tree.add_item(idx, func(val))
        except StopIteration:
            raise ValueError("Not enough input from the generator.")
        tree.build(self.num_tree)
        return tree

    @staticmethod
    def contain_missing_data(feature, num_feat):
        if len(feature) > num_feat:
            return False
        for val in feature:
            if val is None:
                return True
        return False
