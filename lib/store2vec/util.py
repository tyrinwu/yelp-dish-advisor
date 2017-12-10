import sys
sys.path.append("..")
from preprocessing.parser import Parser
import numpy as np


class ReviewParser(Parser):
    def get_review(self, num=10, unlimited=False):
        return self.get_entries(num=num, unlimited=unlimited,
                                func=lambda x: x["text"])

