# -*- coding: utf-8 -*-

from nltk import word_tokenize


class TokenizerBase(object):
    def tokenize(self, text):
        pass


class WordTokenizer(TokenizerBase):
    def tokenize(self, text):
        return word_tokenize(text)
