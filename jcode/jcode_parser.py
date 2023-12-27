"""jcode"""
from pathlib import Path
import os 

from lark import Lark, Transformer
dir_path = Path(os.path.realpath(__file__)).parent

# https://github.com/lark-parser/lark/blob/master/lark/grammars/common.lark
EBNF = (dir_path / "grammar.lark").read_text(encoding="utf-8")


class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]
    def number(self, n):
        (n,) = n
        return float(n)

    list = list
    pair = tuple
    dict = dict

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


class Parser:
    """jcode class"""
    def __init__(self):
        self.ebnf = EBNF
        self._parser = Lark(self.ebnf, start="program")
        self._tree = None
        self._transformer = TreeToJson()
        self._text = ""

    @property
    def parser(self):
        """Get the parser"""
        return self._parser

    @property
    def tree(self):
        """Get the tree"""
        return self._tree

    def __str__(self):
        """Get the string"""
        if self.tree:
            return f"---\n{self._text}\n---\n{self.tree.pretty()}"
        return self._parser

    @property
    def transformer(self):
        """Get the transformer"""
        return self._transformer

    def parse(self, text):
        """parse a string"""
        self._text = text
        self._tree = self._parser.parse(text)
        return self._tree

    def transform(self):
        """Get the transformed value"""
        return self.transformer.transform(self.tree)
