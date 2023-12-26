"""
Unit test
"""
from jcode.jcode_parser import Parser
from lark import Lark

def test_initialize():
    """Test initialization"""
    p = Parser()
    assert isinstance(p, Parser)

def test_parser_type():
    """Test parser type"""
    p = Parser()
    assert isinstance(p.parser, Lark(""))

def test_parsing():
    """test parsing"""
    

# def test_print_string():
#     """Test printing a string"""
#     p = Parser()
#     assert 1 == p.ebnf
