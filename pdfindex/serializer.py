# -*- coding: utf-8 -*-


class SerializerBase(object):
    def serialize(self, index):
        pass;


class MarkdownSerializer(SerializerBase):
    def __init__(self):
        pass

    def serialize(self, index):
        index_sorted = index.get_index_sorted()
        lines = ["# Index"]
        for term, occurrences in index_sorted:
            line = ["* ", term, ": ", ", ".join(map(str, occurrences))]
            lines.append("".join(line))
        return "\n".join(lines)


class HTMLSerializer(SerializerBase):
    def __init__(self):
        pass

    def serialize(self, index):
        index_sorted = index.get_index_sorted()
        lines = ["<html>", "<body>", "<h1>Index</h1>", "<ul>"]
        for term, occurrences in index_sorted:
            line = ["<li><b>", term, "</b>: ", ", ".join(map(str, occurrences))]
            lines.append("".join(line))
        lines.extend(["</ul>", "</body>", "</html>"])
        return "\n".join(lines)
