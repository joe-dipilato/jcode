"""jcode"""
from lark import Lark, Transformer

EBNF = r"""
    ?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS


    """

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
        self._parser = Lark(self.ebnf, start="value")
        self._tree = None
        self._transformer = TreeToJson()

    @property
    def parser(self):
        """Get the parser"""
        return self._parser

    @property
    def tree(self):
        """Get the tree"""
        return self._tree

    @property
    def __str__(self):
        """Get the string"""
        return self.tree.pretty()


    @property
    def transformer(self):
        """Get the transformer"""
        return self._transformer

    def parse(self, text):
        """parse a string"""
        self._tree = self._parser.parse(text)
        return self._tree

    def transform(self):
        """Get the transformed value"""
        return self.transformer.transform(self.tree)
