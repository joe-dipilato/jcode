'''jcode'''
from pathlib import Path

class JCode:
    '''jcode class'''
    def __init__(self):
        self.file = None
        self.raw_content = None

    def parse(self, filename):
        '''parse file'''
        self.file = Path(filename)
        self.raw_content = self.file.read_text()
        return self
    
    def get_file(self):
        '''get the file'''
        return self.file

    def getlines(self):
        '''get all file lines'''
        return self.raw_content.splitlines()
    
    def get_version(self):
        '''get the version of jcode'''
        for line in self.getlines():
            if line.startswith("version:"):
                version = line.split("version:")[1]
                return version
        raise Exception("NoVersion")
        
    def comments(self):
        '''get all comments'''
        return [block for block in self.get_blocks() if block[0].startswith("# ")]

    def starts_block(self, line):
        '''determine if this is a block'''
        return len(line) > 0 and not line.startswith(" ")

    def get_blocks(self):
        '''get the whole block'''
        blocks = []
        block = []
        for line in self.getlines():
            if self.starts_block(line):
                if len(block) > 0:
                    blocks.append(block)
                block = [line]
            else:
                block.append(line)
        blocks.append(block)
        return blocks
