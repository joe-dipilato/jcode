from jcode import JCode
from pathlib import PosixPath

def valid_jcode() -> JCode:
    jc = JCode()
    filename = "jcode/tests/data/valid.jc"
    jc.parse(filename)
    return jc

def invalid_jcode() -> JCode:
    jc = JCode()
    filename = "jcode/tests/data/invalid.jc"
    jc.parse(filename)
    return jc

def test_initialize():
    jc = JCode()
    assert isinstance(jc, JCode)

def test_readfile():
    jc = JCode()
    filename = "jcode/tests/data/valid.jc"
    jc.parse(filename)
    file = jc.get_file()
    assert True == isinstance(file, PosixPath)

def test_validfile():
    jc = JCode()
    filename = "jcode/tests/data/valid.jc"
    valid = jc.parse(filename)
    assert True == valid

def test_invalidfile():
    jc = JCode()
    filename = "jcode/tests/data/invalid.jc"
    valid = jc.parse(filename)
    assert False == valid

def test_get_jcode_file_version():
    jc = valid_jcode()
    version = jc.get_version()
    assert "1.0.0" == version

# def test_get_jcode_invalid_file_version():
#     jc = invalid_jcode()
#     version = jc.get_version()
#     assert "2.0.0" == version

def test_get_comments():
    jc = valid_jcode()
    comments = jc.comments()
    assert "This is a comment" in comments
    assert "This is x comment" not in comments

def test_get_line_count():
    jc = valid_jcode()
    lines = jc.get_lines()
    assert len(lines) == 10