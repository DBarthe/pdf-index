# -*- coding: utf-8 -*-

from __future__ import division
import math


class Chooser(object):
    def __init__(self, score_min):
        self.score_min = score_min

    def score(self, term, doc):
        n_containing = len(filter(lambda page: page.freq_dist.has_key(term), doc.pages))
        max_tf = max(page.freq_dist.freq(term) for page in doc.pages if page.freq_dist.has_key(term))
        idf = math.log(len(doc.pages) / n_containing)
        tfidf = max_tf * idf
        return tfidf

    def choose(self, doc):
        terms_scores = []
        for term in doc.freq_dist.keys():
            score = self.score(term, doc)
            terms_scores.append((term, score))
        return map(lambda x: x[0], filter(lambda x: x[1] >= self.score_min, terms_scores))
