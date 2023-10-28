"""
Unit test
"""

from pathlib import PosixPath, Path
from tempfile import NamedTemporaryFile
from contextlib import contextmanager
from string import ascii_letters
from random import choice, randint

from jcode import JCode

def parse_jc(filename: str):
    """return jcode class"""
    jc = JCode()
    return jc.parse(f"jcode/tests/data/{filename}.ini")

@contextmanager
def tmp_jc(text) -> JCode:
    """Create temporary file"""
    with NamedTemporaryFile(suffix=".ini", prefix="test_") as tmp:
        file = Path(tmp.name)
        file.write_text(text, encoding="utf-8")
        jc = JCode()
        jc.parse(file)
        err = None
        try:
            yield jc
        except Exception as e:
            err = e
        finally:
            if err is not None:
                raise err
        return jc

def rand_text(chars=ascii_letters + " ", minlen=1, maxlen=80):
    """Get rand text"""
    return ''.join(choice(chars) for _ in range(randint(minlen, maxlen)))

def valid_jcode() -> JCode:
    """Parse valid file"""
    jc = parse_jc("valid")
    return jc

def invalid_jcode() -> JCode:
    """parse invalid file"""
    jc = parse_jc("invalid")
    return jc

def test_initialize():
    """Test initialization"""
    jc = JCode()
    assert isinstance(jc, JCode)

def test_readfile():
    """Test if we can read the file"""
    jc = parse_jc("valid")
    file = jc.get_file()
    assert True == isinstance(file, PosixPath)

def test_validfile():
    """Check if parsing returns a correct object"""
    jc = parse_jc("valid")
    assert isinstance(jc, JCode)

def test_invalidfile():
    """Verify handling of invalid file"""
    jc = JCode()
    filename = "jcode/tests/data/validdddddd.jc"
    exception = None
    try:
        jc.parse(filename)
    except FileNotFoundError as e:
        exception = e
    finally:
        assert isinstance(exception, FileNotFoundError)

def test_get_jcode_file_version():
    """Test get_version"""
    jc = parse_jc("get_jcode_file_version")
    version = jc.get_version()
    assert f"634.2563.46623" == version

def test_get_comments():
    """Test the ability to get comments"""
    jc = parse_jc("get_comments")
    comments = jc.comments()
    assert ["# This is x comment"] not in comments
    assert ["# This is a comment"] in comments
    assert [r"# ␓'␊␡␆'$^3`p(w#B]\)u␗␋hR␌*p␃␛W\>e"] in comments
    assert [r"# ␓'␊␡␆'$^5`p(w#B]\)u␗␋hR␌*p␃␛W\>e"] not in comments

def test_get_line_count():
    """Test getting lines"""
    jc = parse_jc("get_line_count")
    lines = jc.getlines()
    assert len(lines) == 3

def test_get_blocks():
    """Test getting blocks"""
    jc = parse_jc("get_blocks")
    blocks = jc.get_blocks()
    assert len(blocks) == 9

def test_get_comment_blocks():
    """Test getting comment blocks"""
    jc = parse_jc("get_comment_blocks")
    blocks = jc.comments()
    assert len(blocks) == 4

def test_print_code():
    """Test printing a string"""
    jc = parse_jc("print_code")
    stdout = jc.code()
    assert stdout == [['1'], ['2'], ['3']]

def test_print_string():
    """Test printing a string"""
    jc = parse_jc("print_string")
    stdout = jc.exec()
    assert stdout == "Hello World!\n"
