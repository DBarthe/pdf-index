# -*- coding: utf-8 -*-
from itertools import groupby


class Index(object):
    def __init__(self):
        self.terms = {}

    def add_term(self, term):
        if term not in self.terms:
            self.terms[term] = []

    def add_occurrence(self, term, page_num):
        self.terms[term].append(page_num)

    def get_index_sorted(self):
        return sorted(list(self.terms.items()), key=lambda item: item[0])

    def get_index_grouped(self):
        return list([(x[0], list(x[1])) for x in groupby(self.get_index_sorted(), lambda x: x[0][0])])

    @staticmethod
    def build(terms, document_analyzed):
        index = Index()
        for term in terms:
            index.add_term(term)
            for page_analysed in document_analyzed.pages:
                if term in page_analysed.freq_dist:
                    index.add_occurrence(term, page_analysed.page.num_page)
        return index


