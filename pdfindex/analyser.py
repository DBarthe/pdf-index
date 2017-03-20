# -*- coding: utf-8 -*-
import nltk
from itertools import chain

from pdfindex import tokenizer, utils
import filters


class Analyser(object):
    def __init__(self):
        self.tokenizer = tokenizer.WordTokenizer()
        self.filters = [
            #filters.debug,
            filters.lowercase,
            filters.trim_special_chars,
            filters.min_length(3)
        ]

    def analyse(self, pdf_text):
        pages_analyzed = map(self.process_page, pdf_text.pages)
        document_analyzed = reduce(lambda d, p: d.add_page(p), pages_analyzed, DocumentAnalyzed())
        return document_analyzed

    def process_page(self, page):
        tokens = self.tokenizer.tokenize(page.raw_text)
        for f in self.filters:
            tokens = Analyser.apply_filter(f, tokens)
        freq_dist = nltk.FreqDist(tokens)
        terms = freq_dist.keys()
        return PageAnalyzed(page, tokens, freq_dist, terms)

    @staticmethod
    def apply_filter(f, tokens):
        return filter(lambda t: t is not None and len(t) > 0, utils.flatten(map(f, tokens)))


class PageAnalyzed(object):
    def __init__(self, page, tokens, freq_dist, terms):
        self.page = page
        self.tokens = tokens
        self.freq_dist = freq_dist
        self.terms = terms


class DocumentAnalyzed(object):
    def __init__(self, pages=None):
        self.pages = []
        self.freq_dist = None
        self.inverse_freq = None

        if pages is not None:
            for page in pages:
                self.add_page(page)

    def add_page(self, page):
        self.pages.append(page)
        if self.freq_dist is None:
            self.freq_dist = page.freq_dist.copy()
        else:
            self.freq_dist += page.freq_dist
        return self
