# -*- coding: utf-8 -*-


import math


class Chooser(object):
    def __init__(self, score_min):
        self.score_min = score_min

    def score(self, term, doc):
        n_containing = len([page for page in doc.pages if term in page.freq_dist])
        max_tf = max(page.freq_dist.freq(term) for page in doc.pages if term in page.freq_dist)
        idf = math.log(len(doc.pages) / n_containing)
        tfidf = max_tf * idf
        return tfidf

    def choose(self, doc):
        terms_scores = []
        for term in list(doc.freq_dist.keys()):
            score = self.score(term, doc)
            terms_scores.append((term, score))
        return [x[0] for x in [x for x in terms_scores if x[1] >= self.score_min]]
