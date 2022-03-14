# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileReader

from pdfindex.pdf import PDFPageText, PDFText


class ExtractorBase(object):
    def extract(self):
        pass


class PDFExtractor(object):
    def __init__(self, stream, page_offset):
        self.stream = stream
        self.reader = None
        self.pdf_text = None
        self.num_pages = None
        self.page_offset = page_offset

    def extract(self):
        self.reader = PdfFileReader(self.stream)
        self.pdf_text = PDFText()
        self.num_pages = self.reader.getNumPages()
        for num_page in range(self.num_pages):
            page = self._extract_page(num_page)
            self.pdf_text.add_page(page)
        return self.pdf_text

    def _extract_page(self, num_page):
        page = self.reader.getPage(num_page)
        raw_text = page.extractText()
        return PDFPageText(num_page + self.page_offset, raw_text)