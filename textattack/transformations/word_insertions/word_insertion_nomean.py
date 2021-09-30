"""
Word Insertion
============================================
Word Insertion transformations act by inserting a new word at a specific word index.
For example, if we insert "new" in position 3 in the text "I like the movie", we get "I like the new movie".
Subclasses can implement the abstract ``WordInsertion`` class by overriding ``self._get_new_words``.
"""
from .word_insertion import WordInsertion
import os
import random

class WordInsertionNoMean(WordInsertion):
    """A base class for word insertions."""

    def _get_new_words(self, current_text, index):
        """Returns a set of new words we can insert at position `index` of `current_text`
        Args:
            current_text (AttackedText): Current text to modify.
            index (int): Position in which to insert a new word
        Returns:
            list[str]: List of new words to insert.
        """
        path = os.path.dirname(os.path.realpath(__file__))
        temp = path.split('/')[:-2]
        filepath = '/'.join(temp) + "/datas/nomean/"
        with open(filepath+'nomean.txt') as f:
            nomean=f.readlines()
        cand=[]
        for i in nomean:
            i = i.strip('\n')
            cand.append(i)
        return random.sample(cand,5)

