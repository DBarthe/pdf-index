# -*- coding: utf-8 -*-


class Index(object):
    def __init__(self):
        self.terms = {}

    def add_term(self, term):
        if term not in self.terms:
            self.terms[term] = []

    def add_occurrence(self, term, page_num):
        self.terms[term].append(page_num)

    def get_index_sorted(self):
        return sorted(self.terms.items(), key=lambda item: item[0])

    @staticmethod
    def build(terms, document_analyzed):
        index = Index()
        for term in terms:
            index.add_term(term)
            for page_analysed in document_analyzed.pages:
                if page_analysed.freq_dist.has_key(term):
                    index.add_occurrence(term, page_analysed.page.num_page)
        return index


