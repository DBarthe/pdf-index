# -*- coding: utf-8 -*-

from pdfindex.analyser import Analyser
from pdfindex.extractor import PDFExtractor
from pdfindex.chooser import Chooser
from pdfindex.index import Index
from pdfindex.serializer import MarkdownSerializer, HTMLSerializer


def main():
    stream = open('./samples/rsx.pdf', 'rb')

    extractor = PDFExtractor(stream)
    analyser = Analyser()
    chooser = Chooser()
    serializer = HTMLSerializer()

    pdf_text = extractor.extract()
    document_analyzed = analyser.analyse(pdf_text)
    terms_selected = chooser.choose(document_analyzed)
    index = Index.build(terms_selected, document_analyzed)
    output = serializer.serialize(index)

    fout = open('output.html', 'w')
    fout.write(output.encode("utf-8"))
    fout.close()
