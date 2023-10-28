"""jcode"""
from lark import Lark

EBNF = r"""
value: dict
     | list
     | ESCAPED_STRING
     | SIGNED_NUMBER
     | "true" | "false" | "null"

list : "[" [value ("," value)*] "]"

dict : "{" [pair ("," pair)*] "}"
pair : ESCAPED_STRING ":" value

%import common.ESCAPED_STRING
%import common.SIGNED_NUMBER
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
