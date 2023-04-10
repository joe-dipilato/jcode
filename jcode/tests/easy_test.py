from jcode import JCode
from pathlib import PosixPath, Path
from tempfile import NamedTemporaryFile
from contextlib import contextmanager
from string import ascii_letters, digits
from random import choice, randint
@contextmanager
def tmp_jc(text) -> JCode:
    with NamedTemporaryFile(suffix=".jc", prefix="test_") as tmp:
        file = Path(tmp.name)
        file.write_text(text)
        jc = JCode()
        jc.parse(file)
        err = None
        try:
            yield jc
        except Exception as e:
            err = e
        finally:
            if err is None:
                return
            else:
                raise err

def rand_text(chars=ascii_letters + " ", minlen=1, maxlen=80):
    return ''.join(choice(chars) for _ in range(randint(minlen, maxlen)))

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
    result = jc.parse(filename)
    assert isinstance(result, JCode)

def test_invalidfile():
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
    digit = rand_text(chars=digits, maxlen=1)
    text = f"""
version:{digit}.0.4
"""
    with tmp_jc(text) as jc:
        version = jc.get_version()
        assert f"{digit}.0.4" == version

# def test_get_jcode_invalid_file_version():
#     jc = invalid_jcode()
#     version = jc.get_version()
#     assert "2.0.0" == version

def test_get_comments():
    r = rand_text(minlen=20)
    r2 = rand_text(minlen=100, maxlen=100)
    text = f"""
# This is a comment
# {r}
"""
    with tmp_jc(text) as jc:
        comments = list(jc.comments())
        assert "This is x comment" not in comments
        assert "This is a comment" in comments
        assert r in comments
        assert r2 not in comments

def test_get_line_count():
    jc = valid_jcode()
    lines = jc.getlines()
    assert len(lines) == 2