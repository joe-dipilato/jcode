"""jcode"""
from lark import Lark

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

class Parser:
    """jcode class"""
    def __init__(self):
        self.ebnf = EBNF
        self._parser = Lark(self.ebnf, start="value")

    @property
    def parser(self):
        """Get the parser"""
        return self._parser

    def parse(self, text):
        """parse a string"""
        return self._parser.parse(text)
