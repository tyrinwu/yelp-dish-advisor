import util_geo
from annoy import AnnoyIndex
import heapq
import numpy as np
from math import sqrt
from geopy.exc import GeocoderServiceError


NUM_FEATURE = 300

class YelpQuery(object):
    def __init__(self, address, preferences, loc_tree, style_tree):
        self.address = address
        self.preferences = preferences
        self.loc_tree = loc_tree
        self.style_tree = style_tree
        self.style_vec = self.style2vec()

    def find_loc_close_stores(self, num_matches):
        try:
            gps_coordinates = util_geo.get_gps_crd(self.address)
            return self.loc_tree.get_nns_by_vector(gps_coordinates, num_matches)
        except GeocoderServiceError:
            print("error occur in geopy. We return a false geolocation.")
            return (-37,89)

    def style2vec(self):
        """ Note that input must be split by ','""" ###
        words = [v.strip() for v in self.preferences.split(",")]
        # word2feat # TODO
        return 1 * (np.random.rand(NUM_FEATURE) > 0.95)

    def get_distance(self, vec):
        return sqrt(sum((self.style_vec[i]-vec[i])**2 for i in range(NUM_FEATURE)))

    def find_style_close_stores(self, num_loc=200, num_style=15):
        close_stores = self.find_loc_close_stores(num_loc)
        h = []
        for item in close_stores:
            vec = self.style_tree.get_item_vector(item)
            heapq.heappush(h, (self.get_distance(vec), item))
        return [heapq.heappop(h) for _ in range(num_style)]



if __name__ == "__main__":
    loc = AnnoyIndex(2)
    loc.load("nnsearch/test.ann")
    style = AnnoyIndex(NUM_FEATURE)
    style.load("nnsearch/test_huge_vec.ann")
    print(style.get_item_vector(1))
    type(style)
    print(loc.get_n_items())

    while True:
        location = input("Where: ")
        style_input = input("Style (split by ',': ")
        query = YelpQuery(location, style_input, loc, style)
        print(query.find_style_close_stores())
