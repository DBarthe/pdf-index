# -*- coding: utf-8 -*-


class Chooser(object):

    def __init__(self):
        pass

    def choose(self, document_analyzed):
        return document_analyzed.freq_dist.keys()
