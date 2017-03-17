# -*- coding: utf-8 -*-


class PDFText:
    def __init__(self):
        self.pages = []

    def add_page(self, page_text):
        self.pages.append(page_text)


class PDFPageText:
    def __init__(self, num_page, raw_text=None):
        self.num_page = num_page
        self.raw_text = raw_text
        self.tokens = None
        self.terms = None
