# -*- coding: utf-8 -*-

import argparse

from pdfindex.analyser import Analyser
from pdfindex.extractor import PDFExtractor
from pdfindex.chooser import Chooser
from pdfindex.index import Index
from pdfindex.serializer import MarkdownSerializer, HTMLSerializer


def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF file and generate a ready-to-print index")
    parser.add_argument("input_file", help="the PDF file")
    parser.add_argument("output_file", help="the output file")
    parser.add_argument("-m", "--min-score", dest="min_score",
                        nargs=1,
                        type=float,
                        action="store",
                        default=[0.1],
                        help="the minimum tfidf score required to be included in the index")
    parser.add_argument("-f", "--format",
                        nargs=1,
                        action="store",
                        default=["html"],
                        choices=["html", "markdown"],
                        help="the output format")
    parser.add_argument("-p", "--page-offset",
                        dest="page_offset",
                        nargs=1,
                        type=int,
                        action="store",
                        default=[1],
                        help="the start of page numbering")

    args = parser.parse_args()
    stream = open(args.input_file, 'rb')
    extractor = PDFExtractor(stream, args.page_offset[0])
    analyser = Analyser()
    serializer = {
        'html': HTMLSerializer,
        'markdown': MarkdownSerializer
    }[args.format[0]]()
    chooser = Chooser(score_min=args.min_score[0])

    pdf_text = extractor.extract()
    document_analyzed = analyser.analyse(pdf_text)
    terms_selected = chooser.choose(document_analyzed)
    index = Index.build(terms_selected, document_analyzed)
    output = serializer.serialize(index)
    fout = open(args.output_file, 'wb')
    fout.write(output.encode("utf-8"))
    fout.close()
