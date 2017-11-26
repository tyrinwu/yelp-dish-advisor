import util_geo
from annoy import AnnoyIndex
import heapq


class YelpQuery(object):
    geo_ann_fn = "here"
    loc_tree = AnnoyIndex(2)
    loc_tree.load(geo_ann_fn)
    style_tree = AnnoyIndex(300) # TODO
    style_tree.load(style_ann_fn)
    def __init__(self, address, preferences):
        self.address = address
        self.preferences = preferences

    def find_loc_close_stores(self, num_matches):
        gps_coordinates = util_geo.get_gps_crd(self.address)
        return loc_tree.get_nns_by_vector(gps_coordinates, num_matches)

    def find_style_close_stores(self, num_loc=200, num_style=15):
        close_stores = self.find_loc_close_stores(num_loc)
        h = []
        i = self.style2vec()
        for store in close_stores:
             heapq.heappush(h, (style_tree.get_distance(i, store), store))
        return [heapq.heappop(h) for _ in range(num_style)]

    def style2vec(self):
        """ Note that input must be split by ','"""
        words = [v.strip() for v in self.preferences.split(",")]
        # word2feat # TODO




