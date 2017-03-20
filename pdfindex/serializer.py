# -*- coding: utf-8 -*-


class SerializerBase(object):
    def serialize(self, index):
        pass;


class SerializerHandler(object):
    def start_index(self):
        pass

    def end_index(self):
        pass

    def start_letter(self, letter):
        pass

    def end_letter(self, letter):
        pass

    def term(self, term, page_nums):
        pass

    def output(self):
        pass


class SerializerTemplate(SerializerBase):
    HANDLER_CTOR = SerializerHandler

    def serialize(self, index):
        handler = self.HANDLER_CTOR()
        handler.start_index()
        for letter, terms_pages in index.get_index_grouped():
            handler.start_letter(letter)
            for term, page_nums in terms_pages:
                handler.term(term, page_nums)
            handler.end_letter(letter)
        handler.end_index()
        return handler.output()


class MarkdownHandler(SerializerHandler):
    def __init__(self):
        self.lines = []

    def start_index(self):
        self.lines.append("# Index")

    def start_letter(self, letter):
        self.lines.append("### %s" % letter)

    def term(self, term, page_nums):
        self.lines.append("* %s: %s" % (term, ", ".join(map(str, page_nums))))

    def output(self):
        return "\n".join(self.lines) + "\n"


class MarkdownSerializer(SerializerTemplate):
    HANDLER_CTOR = MarkdownHandler


class HTMLHandler(SerializerHandler):
    def __init__(self):
        self.lines = []

    def start_index(self):
        self.lines.extend(["<html>", "<body>", "<h1>Index</h1>"])

    def end_index(self):
        self.lines.extend(["</body>", "</html>"])

    def start_letter(self, letter):
        self.lines.append("<h3>%s</h3><ul>" % letter.upper())

    def end_letter(self, letter):
        self.lines.append("</ul>")

    def term(self, term, page_nums):
        self.lines.append("<li>%s: %s</li>" % (term, ", ".join(map(str, page_nums))))

    def output(self):
        return "\n".join(self.lines) + "\n"


class HTMLSerializer(SerializerTemplate):
    HANDLER_CTOR = HTMLHandler
