"""
Word Swap by swapping synonyms in WordNet
==========================================================
"""


import textattack
from collections import defaultdict
from .word_swap import WordSwap
from pypinyin import pinyin, lazy_pinyin

class WordSwapChinesePinyin(WordSwap):
    """Transforms an input by replacing its words with synonyms provided by
    WordNet."""

    def _get_replacement_words(self, word):
        """Returns a list containing all possible words with 1 character
        replaced by a homoglyph."""

        return lazy_pinyin(word)
