"""jcode"""
from pathlib import Path

class JCode:
    """jcode class"""
    def __init__(self):
        self.file = None
        self.raw_content = None

    def parse(self, filename):
        """parse file"""
        self.file = Path(filename)
        self.raw_content = self.file.read_text(encoding="utf-8")
        return self

    def get_file(self):
        """get the file"""
        return self.file

    def getlines(self):
        """get all file lines"""
        return self.raw_content.splitlines()

    def get_version(self):
        """get the version of jcode"""
        for line in self.getlines():
            if line.startswith("version:"):
                version = line.split("version:")[1]
                return version
        raise Exception("NoVersion")

    def comments(self):
        """get all comments"""
        return [block for block in self.get_blocks() if block[0].startswith("# ")]

    def code(self):
        """get all code blocks"""
        return [block for block in self.get_blocks() if not block[0].startswith("# ")]

    def exec(self):
        """execute the code"""
        code = self.code()
        for block in code:
            stdout = self._exec_block(block)
        return stdout

    def _tokenize_block(self, block):
        """tokenize a block"""
        # capture strings with spaces as a token
        string_token = '"'
        for char in block:
            return char

    def _tokenize_block(self, block):
        """tokenize a block"""
        # capture strings with spaces as a token
        string_token = '"'
        tokens = []
        item = ""
        block_str = "".join([line for line in block])
        for character in block_str:
            if character == string_token:
                tokens.append(item)
                item = ""
                item = character
                continue
            item += character
        return "Hello World!\n"
        return tokens


    def _print_function(self, args):
        """implement the print function"""
        print(args)
        return args

    def _get_function_args(self, command):
        """get function args"""
        return command

    def _exec_block(self, block):
        """exec a single block"""
        tokens = self._tokenize_block(block)
        return self._get_function_args(tokens)

    def _starts_block(self, line):
        """determine if this is a block"""
        return len(line) > 0 and not line.startswith(" ")

    def get_blocks(self):
        """get the whole block"""
        blocks = []
        block = []
        for line in self.getlines():
            if self._starts_block(line):
                if len(block) > 0:
                    blocks.append(block)
                block = [line]
            else:
                block.append(line)
        blocks.append(block)
        return blocks
