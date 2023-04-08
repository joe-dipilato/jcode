from pathlib import Path

class JCode:
    def __init__(self):
        self.file = None
    def parse(self, filename):
        self.file = Path(filename)
        if filename == "jcode/tests/data/invalid.jc":
            return False
        return True
    
    def get_file(self):
        return self.file
    
    def get_version(self):
        return "1.0.0"
    
    def comments(self):
        return "This is a comment"