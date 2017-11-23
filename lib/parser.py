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

    def get_entries(self, num):
        """get `num` entries from the json file"""
        with open(self.file_path, 'rb') as json_file:
            counter = 0
            for line in json_file:
                counter += 1
                if counter == num:
                    break
                yield line 

    def print_entries(self, num):
        """print entries"""
        for i in self.get_entries(num):
            print(i)

    def read_thousand_lines(self):
        """Process 1000 lines a time"""
        with open(self.file_path, 'rb') as json_file:
            l = list()
            counter = 0
            for line in json_file:
                counter += 1
                if counter == 1000:
                    break
                l.append(line)
            return l
    
    def iter_parse(self, list_json):
        """Parse a list of json files"""
        for json in list_json:
            parsed_json = ijson.items(io.BytesIO(json), "")
            yield parsed_json
                

def test():
    """Testing"""
    business = "../data/testParser.json"
    parser = Parser(business)
    for i in parser.get_entries(20):
        pprint(i)


def test_ijson_reader():
    """Testing ijson"""          
    business = "../data/testParser.json"
    parser = Parser(business)
    jsons = parser.read_thousand_lines()
    parser.iter_parse(jsons)
    
    
if __name__ == "__main__":
    # test()
    test_ijson_reader()