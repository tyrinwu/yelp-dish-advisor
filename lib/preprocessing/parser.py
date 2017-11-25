#!/usr/bin/env python3
"""Iteratively parse data
"""
import io
import json
from pprint import pprint


class Parser(object):
    """Iterative Parser

    Args:
        file_path

    Usage:
        Users should call get_entries(num) where num
        is the number of lines one needs.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def _read_lines(self):
        """Return a generator."""
        with open(self.file_path, 'rb') as json_file:
            for line in json_file:
                yield line

    def get_entries(self, num=10, unlimited=False, func=lambda x: x):
        """Get entries.

        One can assign a fix number num or set unlimited to True to generate
        as much as possible. Note this function returns an generator.

        Usage:
            for entry in parser.get_entries():
                doSomething()

            To get a specific field of the json, add a lambda function to do so.

            for latitude in parser.get_entries(func=lambda x: x['latitude']):
                doSomethingWithLatitude()

        """
        counter = 0
        for line in self._read_lines():
            counter += 1
            yield func(json.loads(line))
            # for val in ijson.items(io.BytesIO(line), ""):
            #    yield func(val)
            if unlimited is False and counter >= num:
                break


def test_ijson_reader():
    """Testing ijson"""
    business = "../../data/testParser.json"
    parser = Parser(business)
    jsons = parser.read_lines()
    for i in parser.iter_parse(jsons):
        pprint(i)


def test_get_entries(file_path):
    """"""
    parser = Parser(file_path)
    for i in parser.get_entries(20000):
        print(i)


if __name__ == "__main__":
    # To test the program, chancge the review_path below
    test_path = "/Users/tlw/Desktop/yelp-data/review.json"
    test_get_entries(test_path)
