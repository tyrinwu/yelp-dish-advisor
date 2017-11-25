"""Finding reviews with similar location

"""
import sys
sys.path.append("..")
from build import AnnoyTreeBuilder as atb
from preprocessing import parser

def test_geodistance():
    tree = atb()
    p = parser.Parser("/Users/tlw/Desktop/yelp-data/business.json")
    # tree.build_iter()
    generator = p.get_entries(func=get_loc, unlimited=True)
    t = tree.build_iter("", generator, 2, 100000)
    for j in t.get_nns_by_item(1, 50):
        print(t.get_distance(1,j))

def get_loc(x):
    try:
        return x["latitude"], x["longitude"]
    except KeyError:
        print("....")

test_geodistance()