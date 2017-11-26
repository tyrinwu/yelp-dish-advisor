"""Finding reviews with similar location

"""
import sys
import time
sys.path.append("..")
from build import AnnoyTreeBuilder as atb
from preprocessing import parser
from sentiment.sentiment import get_sentiment
import numpy as np


def test_geodistance():
    def get_loc(x):
        try:
            return x["latitude"], x["longitude"]
        except KeyError:
            print("....")

    tree = atb()
    p = parser.Parser("/Users/tlw/Desktop/yelp-data/business.json")
    generator = p.get_entries(func=get_loc, unlimited=True)
    t = tree.build_iter(generator, 2, 10000000)
    begin = time.time()
    for j in t.get_nns_by_item(1, 50):
        print(t.get_distance(1,j))
    print("---- {}".format(time.time() - begin))
    t.save("test.ann")

def test_sentiment_closeness():
    def get_review_sentimentment(x):
        try:
            return get_sentiment(x['text'])
        except KeyError:
            print("KeyError in get_review_sentiment")
    tree = atb()
    p = parser.Parser("/Users/tlw/Desktop/yelp-data/review.json")
    generator = p.get_entries(unlimited=True)
    t, mapping = tree.build_iter_testing(generator, 2, 1000, func=get_review_sentimentment)
    begin = time.time()
    for j in t.get_nns_by_item(16, 50):
        print("----")
        print(mapping[j][1]["text"])
        print(mapping[j][0])
        print(j)
        print("----")
    print("---------------------------")
    print(mapping[16][1]["text"])
    print(mapping[16][0])
    print("---- {}".format(time.time() - begin))
    t.save("test_sent.ann")


def test_huge_vectors():
    def generate_onezero_vect(num_input):
        for i in range(num_input):
            yield 1 * (np.random.rand(300) > 0.95)
    tree = atb()
    t, mapping = tree.build_iter_testing(generate_onezero_vect(1000000), 300, 1000000)
    begin = time.time()
    for j in t.get_nns_by_item(16, 50):
        print("----")
        print(j)
        print("----")
    print("---------------------------")
    print("---- {}".format(time.time() - begin))
    t.save("test_huge_vec.ann")


if __name__ == "__main__":
    # test_geodistance()
    #test_sentiment_closeness()
    test_huge_vectors()