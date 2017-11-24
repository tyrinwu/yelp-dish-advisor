"""TODO"""
import parser

class MongoDBYelp(object):
    """Port dataset into MongoDB
    Supported Yelp datasets
        - business.json
    """    
    def __init__(self, db_name):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db_in_use = self.client[db_name]
        self.collections = dict()
        
    def set_index(self, collection, key_index):
        """Create index for a collection"""
        self.db_in_use[collection].create_index([(key_index, pymongo.ASCENDING)], unique=True)

    def get_collection(self, collection):
        """Get a collection from a certain database"""
        return self.db_in_use[collection]

    def iter_parse(self, file_path, size=1000):
        parser = Parser(file_path)
        i = 0
        while (i < size):
            for doc in parser.iter_parse(parser.read_thousand_lines()):
                self.get_collection("testing").insert_one(doc)
            i += 1000