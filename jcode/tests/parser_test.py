"""
Unit test
"""
from jcode.jcode_parser import Parser
from lark import Lark, tree

def test_initialize():
    """Test initialization"""
    p = Parser()
    assert isinstance(p, Parser)

def test_parser_type():
    """Test parser type"""
    p = Parser()
    assert isinstance(p.parser, Lark)

def test_parsing():
    """test parsing"""
    text = 'a=1\n'
    p = Parser()
    parsed = p.parse(text)
    assert isinstance(parsed, tree.Tree)
    assert isinstance(p.tree, tree.Tree)

def test_equals():
    """test parsing"""
    text = 'a=1\n'
    p = Parser()
    p.parse(text)

def test_add():
    """test parsing"""
    text = '1==2\n'
    p = Parser()
    p.parse(text)

def test_set_add():
    """test parsing"""
    text = 'a=1==2\n'
    p = Parser()
    p.parse(text)

def test_set_equals():
    """test parsing"""
    text = 'a=1==2\n'
    p = Parser()
    p.parse(text)

def test_multi_statement():
    """test parsing"""
    text = """
a=(1)
b=2
"""
    p = Parser()
    p.parse(text)

def test_set():
    """test parsing"""
    text = """
b=x,y,z
"""
    p = Parser()
    p.parse(text)
    print(p)
    text = """
b
"""
    p = Parser()
    p.parse(text)
    print(p)


# def test_transform():
#     """test transform"""
#     text = '{"key": ["item0", "item1", 3.14]}'
#     p = Parser()
#     p.parse(text)
#     transformed = p.transform()
#     assert isinstance(transformed, dict)
#     assert transformed["key"] == ["item0", "item1", 3.14]
