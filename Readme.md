pdfindex
========

PDF-index is a command line tool that find important terms in a PDF document and generates a ready-to-print index.

It relies on PyPDF and NLTK libraries for extracting and mining text.

Output formats currently supported are HTML and Markdown.

It works with python 2


Example
-----
For generating an html index from the `input.pdf` document to `output.html`, selecting terms with a minimum score of 0.2:
```bash
$ python pdfindex.py --min-score 0.2 --format html input.pdf output.html
```

Usage
-----
Within a virtualenv:
```bash
$ pip install -r requirements.txt
```

Print usage:
```bash
$ python pdfindex.py  -h
usage: pdfindex.py [-h] [-m MIN_SCORE] [-f {html,markdown}] [-p PAGE_OFFSET]
                   input_file output_file

Extract text from a PDF file and generate a ready-to-print index

positional arguments:
  input_file            the PDF file
  output_file           the output file

optional arguments:
  -h, --help            show this help message and exit
  -m MIN_SCORE, --min-score MIN_SCORE
                        the minimum tfidf score required to be included in the
                        index
  -f {html,markdown}, --format {html,markdown}
                        the output format
  -p PAGE_OFFSET, --page-offset PAGE_OFFSET
                        the start of page numbering
```


