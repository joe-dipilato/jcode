from pathlib import Path

class JCode:
    def __init__(self):
        self.file = None
        self.raw_content = None

    def parse(self, filename):
        self.file = Path(filename)
        self.raw_content = self.file.read_text()
        return self
    
    def get_file(self):
        return self.file

    def get_lines(self):
        return self.raw_content.splitlines()
    
    def get_version(self):
        return "1.0.0"
    
    def comments(self):
        yield from (line[2:] for line in self.get_lines() if line.startswith("# "))