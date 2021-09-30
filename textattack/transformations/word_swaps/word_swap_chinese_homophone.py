"""
Word Swap by swapping synonyms in WordNet
==========================================================
"""


import textattack
from collections import defaultdict
from .word_swap import WordSwap
import pickle as pkl
import os
from pypinyin import lazy_pinyin

path = os.path.dirname(os.path.realpath(__file__))
temp = path.split('/')[:-2]
filepath = '/'.join(temp)+"/datas/homophone/"

map={
    "CharHomo":"chinese_homophone_char.txt",
    "WordHomo":"chinese_homophone_word.txt",
}
class TongYin:
    def __init__(self, dict_name):
        self.diction = defaultdict(list)
        if not os.path.exists(filepath+dict_name):
            self.make_dict_pkl(dict_name)
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

    def __call__(self, pinyin):
        return self.diction[pinyin]

class WordSwapChineseHomo(WordSwap):
    """Transforms an input by replacing its words with synonyms provided by
    WordNet."""

    def __init__(self, dict_name="CharHomo"):
        self.tongyin = TongYin(dict_name)

    def _get_replacement_words(self, word):
        """Returns a list containing all possible words with 1 character
        replaced by a homoglyph."""
        pinyin = lazy_pinyin(word)[0]
        return self.tongyin(pinyin)
