"""
Word Swap by swapping synonyms in WordNet
==========================================================
"""


import textattack
from collections import defaultdict
from .word_swap import WordSwap
import pickle as pkl
import os

path = os.path.dirname(os.path.realpath(__file__))
temp = path.split('/')[:-2]
filepath = '/'.join(temp)+"/datas/chaizi/"
map={
    "Simplified":"chaizi-jt.txt",
    "Traditional":"chaizi-ft.txt"
}

class ChaiZi:
    def __init__(self, dict_name):
        self.diction = defaultdict(list)
        print(filepath+dict_name)
        if not os.path.exists(filepath+dict_name):
            self.make_dict_pkl(filepath+dict_name)
        with open(filepath+dict_name, 'rb') as f:
            self.diction.update(pkl.load(f))

    def make_dict_pkl(self,dict_name: str):
        diction = dict()
        with open(filepath+map[dict_name]) as f:
            a = f.readlines()
        for i in a:
            i = i.strip('\n')
            split = i.split("\t")
            diction[split[0]] = [i for i in split[1:]]

        with open(filepath+dict_name, 'wb') as f:
            pkl.dump(diction, f)
    def __call__(self, word):
        return self.diction[word]

class WordSwapChineseSplitChar(WordSwap):
    """Transforms an input by replacing its words with synonyms provided by
    WordNet."""

    def __init__(self, dict_name="Simplified"):
        self.chaizi = ChaiZi(dict_name)

    def _get_replacement_words(self, word):
        """Returns a list containing all possible words with 1 character
        replaced by a homoglyph."""

        return self.chaizi(word)
