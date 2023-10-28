"""
Unit test
"""
from jcode.jcode_parser import Parser

def test_initialize():
    """Test initialization"""
    p = Parser()
    assert isinstance(p, Parser)


# def test_print_string():
#     """Test printing a string"""
#     p = Parser()
#     assert 1 == p.ebnf
