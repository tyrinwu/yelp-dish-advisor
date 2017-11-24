#!/usr/bin/env python3
"""Iteratively parse data into mongoDB
Dependency: ijson
"""
import io
import ijson
from pprint import pprint


class Parser(object):
    """Iterative Parser"""
    def __init__(self, file_path):
        self.file_path = file_path

    def read_lines(self, NUM=1000):
        """Read `num` lines a time and yield it"""
        with open(self.file_path, 'rb') as json_file:
            thousand_lines = list()
            counter = 0
            for line in json_file:
                thousand_lines.append(line)
                counter += 1
                if counter == NUM:
                    yield thousand_lines
                    counter = 0

    @staticmethod
    def iter_parse(list_json):
        """Parse a list of json files"""
        for json in list_json:
            print(json)
            parsed_json = ijson.items(io.BytesIO(json), "")
            for val in parsed_json:
                yield val

    def get_entries(self, num):
        """Get `num` of entries."""
        counter = 0
        for thousand_lines in self.read_thousand_lines():
            print(thousand_lines)
            for entry in self.iter_parse(thousand_lines):
                yield entry
            counter += 1000
            if counter > num:
                break


def test_ijson_reader():
    """Testing ijson"""          
    business = "../../data/testParser.json"
    parser = Parser(business)
    jsons = parser.read_thousand_lines()
    for i in parser.iter_parse(jsons):
        pprint(i)


def test_get_entries(file_path):
    parser = Parser(file_path)
    for i in parser.get_entries(2000):
        pprint(i)


if __name__ == "__main__":
    # test()
    # test_ijson_reader()
    test_get_entries("/Users/tlw/Desktop/yelp-data/10000/review-10000.json")