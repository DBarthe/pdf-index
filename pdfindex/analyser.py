# -*- coding: utf-8 -*-
import nltk

from pdfindex import tokenizer
import filters


class Analyser(object):
    def __init__(self):
        self.tokenizer = tokenizer.WordTokenizer()
        self.filters = [
            filters.lowercase
        ]

    def analyse(self, pdf_text):
        pages_analyzed = map(self.process_page, pdf_text.pages)
        document_analyzed = reduce(lambda d, p: d.add_page(p), pages_analyzed, DocumentAnalyzed())
        return document_analyzed

    def process_page(self, page):
        tokens = self.tokenizer.tokenize(page.raw_text)
        for f in self.filters:
            tokens = filter(lambda t: t is not None, map(f, tokens))
        freq_dist = nltk.FreqDist(tokens)
        terms = freq_dist.keys()
        return PageAnalyzed(page, tokens, freq_dist, terms)


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
