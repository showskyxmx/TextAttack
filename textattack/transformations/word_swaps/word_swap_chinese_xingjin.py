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
filepath = '/'.join(temp)+"/datas/xingjin/"

map={
    "Xingjin":"xingjin.txt"
}

class XingJin:
    def __init__(self, dict_name='Xingjin'):
        self.diction = defaultdict(list)
        if not os.path.exists(filepath+dict_name):
            self.make_dict_pkl(dict_name)
        with open(filepath+dict_name, 'rb') as f:
            self.diction.update(pkl.load(f))

    def make_dict_pkl(self,dict_name: str):
        diction = dict()
        keys = defaultdict(int)
        values = defaultdict(list)
        with open(filepath+map[dict_name]) as f:
            a = f.readlines()
        num = 1
        values['0'] = []
        for i in a:
            i = i.strip('\n')
            split = i.split("，")
            values[num] = split
            for j in split:
                keys[j] = num
            num = num + 1
        diction.update(keys=keys, values=values)
        with open(filepath+dict_name, 'wb') as f:
            pkl.dump(diction, f)

    def __call__(self, word):
        result = self.diction['values'][self.diction['keys'][word]].copy()
        if word in result:
            result.remove(word)
        return result

class WordSwapChineseXingjin(WordSwap):
    """Transforms an input by replacing its words with synonyms provided by
    WordNet."""

    def __init__(self, dict_name="Xingjin"):
        self.xingjin = XingJin(dict_name)

    def _get_replacement_words(self, word):
        """Returns a list containing all possible words with 1 character
        replaced by a homoglyph."""
        return self.xingjin(word)
