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

    def getlines(self):
        return self.raw_content.splitlines()
    
    def get_version(self):
        for line in self.getlines():
            if line.startswith("version:"):
                version = line.split("version:")[1]
                return version
        raise Exception("NoVersion")
        
    
    def comments(self):
        yield from (line[2:] for line in self.getlines() if line.startswith("# "))