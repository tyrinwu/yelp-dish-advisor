"""Iteratively parse data into mongoDB

Dependency: ijson


"""
import ijson


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


def test():
    """Testing"""
    business = "/Users/tlw/Desktop/yelp-data/test.json"
    parser = Parser(business)
    for i in parser.get_entries(20):
        print(i)


if __name__ == "__main__":
    test()
