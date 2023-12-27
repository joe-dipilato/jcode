"""jcode"""
from lark import Lark, Transformer

EBNF2 = r"""
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

# https://github.com/lark-parser/lark/blob/master/lark/grammars/common.lark
EBNF = r"""
    statement : "if" paren_expr statement
              | "if" paren_expr statement "else" statement
              | "while" paren_expr statement
              | "do" statement "while" paren_expr
              | "{" statement* "}"
              | expr
    program : statement+
    paren_expr : "(" expr ")"
    expr : test
         | variable "=" expr
    test : sum
         | greater_than
         | less_than
         | equals_to
    greater_than : sum ">" sum
    less_than : sum "<" sum
    equals_to : sum "==" sum
    sum : term
        | sum "+" term
        | sum "-" term
    term : variable
       | integer
       | paren_expr
    variable : CNAME
    integer : INT
    STRING : ESCAPED_STRING

    %import common.CNAME
    %import common.ESCAPED_STRING
    %import common.INT
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
